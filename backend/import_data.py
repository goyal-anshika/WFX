import os
from pathlib import Path

import pandas as pd
import psycopg2
from dotenv import load_dotenv


# =========================================================
# CONFIGURATION
# =========================================================

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is missing from .env")


DATA_DIR = Path("data/ready")


# =========================================================
# LOAD CSV FILES
# =========================================================

buyers = pd.read_csv(DATA_DIR / "buyers_ready.csv")
suppliers = pd.read_csv(DATA_DIR / "suppliers_ready.csv")
finished_goods = pd.read_csv(
    DATA_DIR / "finished_goods_ready.csv"
)
tech_packs = pd.read_csv(
    DATA_DIR / "tech_packs_ready.csv"
)
sales_orders = pd.read_csv(
    DATA_DIR / "sales_orders_ready.csv"
)
sales_invoices = pd.read_csv(
    DATA_DIR / "sales_invoices_ready.csv"
)


print("CSV files loaded successfully.")
print()


# =========================================================
# CONNECT TO DATABASE
# =========================================================

print("Connecting to Supabase PostgreSQL...")

connection = psycopg2.connect(DATABASE_URL)

connection.autocommit = False

cursor = connection.cursor()

print("Database connection successful.")
print()


try:

    # =====================================================
    # 1. SUPPLIERS
    # =====================================================

    print("Importing suppliers...")

    for _, row in suppliers.iterrows():

        cursor.execute(
            """
            INSERT INTO public.suppliers
            (
                supplier_id,
                company_name,
                country,
                contact,
                lead_time_days,
                rating
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (supplier_id)
            DO NOTHING
            """,
            (
                row["supplier_id"],
                row["company_name"],
                row["country"],
                row["contact"],
                row["lead_time_days"],
                row["rating"],
            ),
        )

    print(f"Suppliers processed: {len(suppliers)}")


    # =====================================================
    # 2. BUYERS
    # =====================================================

    print("Importing buyers...")

    for _, row in buyers.iterrows():

        cursor.execute(
            """
            INSERT INTO public.buyers
            (
                buyer_id,
                company_name,
                country,
                buyer_category
            )
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (buyer_id)
            DO NOTHING
            """,
            (
                row["buyer_id"],
                row["company_name"],
                row["country"],
                row["buyer_category"],
            ),
        )

    print(f"Buyers processed: {len(buyers)}")


    # =====================================================
    # 3. BUILD SUPPLIER LOOKUP
    # =====================================================

    cursor.execute(
        """
        SELECT id, supplier_id
        FROM public.suppliers
        """
    )

    supplier_lookup = {
        supplier_id: db_id
        for db_id, supplier_id in cursor.fetchall()
    }


    # =====================================================
    # 4. FINISHED GOODS
    # =====================================================

    print("Importing finished goods...")

    for _, row in finished_goods.iterrows():

        supplier_db_id = supplier_lookup.get(
            row["supplier_id"]
        )

        if supplier_db_id is None:
            raise ValueError(
                f"Supplier not found: {row['supplier_id']}"
            )

        cursor.execute(
            """
            INSERT INTO public.finished_goods
            (
                style_number,
                style_name,
                category,
                fabric,
                gsm,
                color,
                print,
                season,
                brand,
                supplier_id,
                cost,
                selling_price,
                image_url
            )
            VALUES
            (
                %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s
            )
            ON CONFLICT (style_number)
            DO NOTHING
            """,
            (
                row["style_number"],
                row["style_name"],
                row["category"],
                row["fabric"],
                row["gsm"],
                row["color"],
                row["print"],
                row["season"],
                row["brand"],
                supplier_db_id,
                row["cost"],
                row["selling_price"],
                row["image_url"],
            ),
        )

    print(
        f"Finished goods processed: "
        f"{len(finished_goods)}"
    )


    # =====================================================
    # 5. TECH PACKS
    # =====================================================

    print("Importing tech packs...")

    for _, row in tech_packs.iterrows():

        cursor.execute(
            """
            INSERT INTO public.tech_packs
            (
                tech_pack_id,
                style_number,
                fabric_details,
                construction,
                wash_instructions
            )
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (tech_pack_id)
            DO NOTHING
            """,
            (
                row["tech_pack_id"],
                row["style_number"],
                row["fabric_details"],
                row["construction"],
                row["wash_instructions"],
            ),
        )

    print(
        f"Tech packs processed: "
        f"{len(tech_packs)}"
    )


    # =====================================================
    # 6. BUILD BUYER LOOKUP
    # =====================================================

    cursor.execute(
        """
        SELECT id, buyer_id
        FROM public.buyers
        """
    )

    buyer_lookup = {
        buyer_id: db_id
        for db_id, buyer_id in cursor.fetchall()
    }


    # =====================================================
    # 7. BUILD STYLE LOOKUP
    # =====================================================

    cursor.execute(
        """
        SELECT id, style_number
        FROM public.finished_goods
        """
    )

    style_lookup = {
        style_number: db_id
        for db_id, style_number in cursor.fetchall()
    }


    # =====================================================
    # 8. SALES ORDERS
    # =====================================================

    print("Importing sales orders...")

    for _, row in sales_orders.iterrows():

        buyer_db_id = buyer_lookup.get(
            row["buyer_id"]
        )

        if buyer_db_id is None:
            raise ValueError(
                f"Buyer not found: {row['buyer_id']}"
            )

        if row["style_number"] not in style_lookup:
            raise ValueError(
                f"Style not found: {row['style_number']}"
            )

        cursor.execute(
            """
            INSERT INTO public.sales_orders
            (
                order_number,
                buyer_id,
                style_number,
                quantity,
                unit_price,
                shipment_date,
                status
            )
            VALUES
            (
                %s, %s, %s, %s, %s, %s, %s
            )
            ON CONFLICT (order_number)
            DO NOTHING
            """,
            (
                row["order_number"],
                buyer_db_id,
                row["style_number"],
                row["quantity"],
                row["unit_price"],
                row["shipment_date"],
                row["status"],
            ),
        )

    print(
        f"Sales orders processed: "
        f"{len(sales_orders)}"
    )


    # =====================================================
    # 9. BUILD ORDER LOOKUP
    # =====================================================

    cursor.execute(
        """
        SELECT id, order_number
        FROM public.sales_orders
        """
    )

    order_lookup = {
        order_number: db_id
        for db_id, order_number in cursor.fetchall()
    }


    # =====================================================
    # 10. SALES INVOICES
    # =====================================================

    print("Importing sales invoices...")

    for _, row in sales_invoices.iterrows():

        order_db_id = order_lookup.get(
            row["sales_order"]
        )

        if order_db_id is None:
            raise ValueError(
                f"Sales order not found: "
                f"{row['sales_order']}"
            )

        cursor.execute(
            """
            INSERT INTO public.sales_invoices
            (
                invoice_number,
                sales_order_id,
                amount,
                currency,
                payment_status
            )
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (invoice_number)
            DO NOTHING
            """,
            (
                row["invoice_number"],
                order_db_id,
                row["amount"],
                row["currency"],
                row["payment_status"],
            ),
        )

    print(
        f"Sales invoices processed: "
        f"{len(sales_invoices)}"
    )


    # =====================================================
    # COMMIT
    # =====================================================

    connection.commit()

    print()
    print("=" * 60)
    print("DATA IMPORT COMPLETED SUCCESSFULLY")
    print("=" * 60)


except Exception as error:

    connection.rollback()

    print()
    print("=" * 60)
    print("IMPORT FAILED")
    print("=" * 60)
    print()
    print(error)
    print()
    print("All changes have been rolled back.")

    raise


finally:

    cursor.close()
    connection.close()

    print()
    print("Database connection closed.")
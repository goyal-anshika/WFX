import pandas as pd
from pathlib import Path


# =========================================================
# PATHS
# =========================================================

DATA_DIR = Path("data")
OUTPUT_DIR = DATA_DIR / "ready"

OUTPUT_DIR.mkdir(exist_ok=True)


# =========================================================
# LOAD ORIGINAL CSV FILES
# =========================================================

buyers = pd.read_csv(DATA_DIR / "buyers.csv")
suppliers = pd.read_csv(DATA_DIR / "suppliers.csv")
finished_goods = pd.read_csv(DATA_DIR / "finished_goods.csv")
tech_packs = pd.read_csv(DATA_DIR / "tech_packs.csv")
sales_orders = pd.read_csv(DATA_DIR / "sales_orders.csv")
sales_invoices = pd.read_csv(DATA_DIR / "sales_invoices.csv")


print("Original data loaded successfully.")
print()


# =========================================================
# 1. BUYERS
# =========================================================

buyers_ready = buyers[
    [
        "buyer_id",
        "company_name",
        "country",
        "buyer_category"
    ]
].copy()


# =========================================================
# 2. SUPPLIERS
# =========================================================

suppliers_ready = suppliers[
    [
        "supplier_id",
        "company_name",
        "country",
        "contact",
        "lead_time_days",
        "rating"
    ]
].copy()


# =========================================================
# 3. FINISHED GOODS
#
# Convert supplier company name → supplier_id
# =========================================================

supplier_lookup = suppliers.set_index("company_name")["supplier_id"]

finished_goods_ready = finished_goods.copy()

finished_goods_ready["supplier_id"] = (
    finished_goods_ready["supplier"]
    .map(supplier_lookup)
)


# Check for suppliers that could not be matched
missing_suppliers = finished_goods_ready[
    finished_goods_ready["supplier_id"].isna()
]

if not missing_suppliers.empty:
    print("ERROR: Some finished goods have unknown suppliers:")
    print(missing_suppliers["supplier"].unique())
    raise ValueError("Supplier mapping failed.")


finished_goods_ready = finished_goods_ready[
    [
        "style_number",
        "style_name",
        "category",
        "fabric",
        "gsm",
        "color",
        "print",
        "season",
        "brand",
        "supplier_id",
        "cost",
        "selling_price",
        "image_url"
    ]
]


# =========================================================
# 4. TECH PACKS
# =========================================================

tech_packs_ready = tech_packs[
    [
        "tech_pack_id",
        "style_number",
        "fabric_details",
        "construction",
        "wash_instructions"
    ]
].copy()


# =========================================================
# 5. SALES ORDERS
#
# Convert buyer company name → buyer_id
# =========================================================

buyer_lookup = buyers.set_index("company_name")["buyer_id"]

sales_orders_ready = sales_orders.copy()

sales_orders_ready["buyer_id"] = (
    sales_orders_ready["buyer"]
    .map(buyer_lookup)
)


# Check for buyers that could not be matched
missing_buyers = sales_orders_ready[
    sales_orders_ready["buyer_id"].isna()
]

if not missing_buyers.empty:
    print("ERROR: Some sales orders have unknown buyers:")
    print(missing_buyers["buyer"].unique())
    raise ValueError("Buyer mapping failed.")


sales_orders_ready = sales_orders_ready[
    [
        "order_number",
        "buyer_id",
        "style_number",
        "quantity",
        "unit_price",
        "shipment_date",
        "status"
    ]
]


# =========================================================
# 6. SALES INVOICES
#
# Convert sales order number → later database relationship
#
# For now we preserve sales_order as the business ID.
# We will map it to the Supabase UUID after importing
# sales orders.
# =========================================================

sales_invoices_ready = sales_invoices[
    [
        "invoice_number",
        "sales_order",
        "amount",
        "currency",
        "payment_status"
    ]
].copy()


# =========================================================
# VALIDATION
# =========================================================

print("Validating data...")
print()

print(f"Buyers:          {len(buyers_ready)}")
print(f"Suppliers:       {len(suppliers_ready)}")
print(f"Finished Goods:  {len(finished_goods_ready)}")
print(f"Tech Packs:      {len(tech_packs_ready)}")
print(f"Sales Orders:    {len(sales_orders_ready)}")
print(f"Sales Invoices:  {len(sales_invoices_ready)}")

print()


# Check duplicate primary/business IDs

checks = {
    "buyer_id": buyers_ready["buyer_id"],
    "supplier_id": suppliers_ready["supplier_id"],
    "style_number": finished_goods_ready["style_number"],
    "tech_pack_id": tech_packs_ready["tech_pack_id"],
    "order_number": sales_orders_ready["order_number"],
    "invoice_number": sales_invoices_ready["invoice_number"],
}

for column, values in checks.items():
    duplicates = values[values.duplicated()]

    if not duplicates.empty:
        print(f"ERROR: Duplicate {column} values found:")
        print(duplicates.tolist())
        raise ValueError(f"Duplicate {column} values found.")


print("No duplicate primary/business IDs found.")


# =========================================================
# SAVE READY FILES
# =========================================================

buyers_ready.to_csv(
    OUTPUT_DIR / "buyers_ready.csv",
    index=False
)

suppliers_ready.to_csv(
    OUTPUT_DIR / "suppliers_ready.csv",
    index=False
)

finished_goods_ready.to_csv(
    OUTPUT_DIR / "finished_goods_ready.csv",
    index=False
)

tech_packs_ready.to_csv(
    OUTPUT_DIR / "tech_packs_ready.csv",
    index=False
)

sales_orders_ready.to_csv(
    OUTPUT_DIR / "sales_orders_ready.csv",
    index=False
)

sales_invoices_ready.to_csv(
    OUTPUT_DIR / "sales_invoices_ready.csv",
    index=False
)


print()
print("Data preparation completed successfully.")
print(f"Ready files created in: {OUTPUT_DIR}")
from app.services.llm_service import ask_llm


SCHEMA = """
PostgreSQL database schema for the WFX ERP system.

TABLE: suppliers
- id UUID PRIMARY KEY
- company_name TEXT
- country TEXT
- contact TEXT
- lead_time INTEGER
- rating NUMERIC

TABLE: buyers
- id UUID PRIMARY KEY
- company_name TEXT
- country TEXT
- buyer_category TEXT

TABLE: finished_goods
- id UUID PRIMARY KEY
- style_number TEXT UNIQUE
- style_name TEXT
- category TEXT
- fabric TEXT
- gsm NUMERIC
- color TEXT
- print TEXT
- season TEXT
- brand TEXT
- supplier_id UUID REFERENCES suppliers(id)
- cost NUMERIC
- selling_price NUMERIC
- image_url TEXT

TABLE: sales_orders
- id UUID PRIMARY KEY
- order_number TEXT UNIQUE
- buyer_id UUID REFERENCES buyers(id)
- quantity INTEGER
- shipment_date DATE
- status TEXT

TABLE: tech_packs
- id UUID PRIMARY KEY
- style_number TEXT REFERENCES finished_goods(style_number)
- fabric_details TEXT
- construction TEXT
- wash_instructions TEXT

TABLE: sales_invoices
- id UUID PRIMARY KEY
- invoice_number TEXT UNIQUE
- sales_order_id UUID REFERENCES sales_orders(id)
- amount NUMERIC
- currency TEXT
- payment_status TEXT

RELATIONSHIPS:

buyers.id = sales_orders.buyer_id

sales_orders.id = sales_invoices.sales_order_id

suppliers.id = finished_goods.supplier_id

finished_goods.style_number = tech_packs.style_number
"""


def generate_sql(question: str) -> str:

    prompt = f"""
You are an expert PostgreSQL SQL generator.

You are working with the following WFX ERP database:

{SCHEMA}

Convert the user's question into ONE PostgreSQL SELECT query.

Rules:
1. Generate SELECT statements only.
2. Never generate INSERT, UPDATE, DELETE, DROP, ALTER, CREATE or TRUNCATE.
3. Use only the tables and columns provided.
4. Use proper PostgreSQL syntax.
5. Return ONLY the SQL query.
6. Do not use markdown.
7. Do not explain the query.

User question:
{question}
"""

    return ask_llm(prompt).strip()
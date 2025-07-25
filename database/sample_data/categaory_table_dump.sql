
"""
categorise and organise transactions
"""
CREATE TABLE categories (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL CHECK (type IN ('Income', 'Expense', 'Savings', 'Investment', 'Other', 'Unknown', 'Timebound'))
);

INSERT INTO categories (id, name, type) VALUES
  ('00000000-0000-0000-0000-000000000001', 'Salary', 'Income'),
  ('00000000-0000-0000-0000-000000000002', 'Freelance', 'Income'),
  ('00000000-0000-0000-0000-000000000003', 'Groceries', 'Expense'),
  ('00000000-0000-0000-0000-000000000004', 'Rent', 'Expense'),
  ('00000000-0000-0000-0000-000000000005', 'Utilities', 'Expense'),
  ('00000000-0000-0000-0000-000000000006', 'Dining Out', 'Expense'),
  ('00000000-0000-0000-0000-000000000007', 'Savings Account', 'Savings'),
  ('00000000-0000-0000-0000-000000000008', 'Emergency Fund', 'Savings'),
  ('00000000-0000-0000-0000-000000000009', 'Stocks', 'Investment'),
  ('00000000-0000-0000-0000-000000000010', 'Mutual Funds', 'Investment'),
  ('00000000-0000-0000-0000-000000000011', 'Car Insurance', 'Timebound'),
  ('00000000-0000-0000-0000-000000000012', 'Annual Subscriptions', 'Timebound'),
  ('00000000-0000-0000-0000-000000000013', 'Miscellaneous', 'Other'),
  ('00000000-0000-0000-0000-000000000014', 'Uncategorized', 'Unknown');


"""
currencies to handle in the application
"""
CREATE TABLE currencies (
      id UUID PRIMARY KEY,
      name TEXT NOT NULL,              -- Full name (e.g., Indian Rupee)
      code TEXT NOT NULL UNIQUE,       -- ISO code (e.g., INR, USD, GBP)
      symbol TEXT NOT NULL             -- ₹, $, £, etc.
  );


INSERT INTO currencies (id, name, code, symbol) VALUES
    ('11111111-1111-1111-1111-111111111001', 'Indian Rupee', 'INR', '₹'),
    ('11111111-1111-1111-1111-111111111002', 'US Dollar', 'USD', '$'),
    ('11111111-1111-1111-1111-111111111003', 'British Pound', 'GBP', '£'),
    ('11111111-1111-1111-1111-111111111004', 'Euro', 'EUR', '€');

CREATE TABLE transactions (
        id UUID PRIMARY KEY,
        amount NUMERIC NOT NULL,
        currency_id UUID NOT NULL REFERENCES currencies(id),
        type_id UUID REFERENCES transaction_types(id),
        category_id UUID REFERENCES categories(id),
        date DATE NOT NULL,
        note TEXT,
        is_active BOOLEAN DEFAULT TRUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

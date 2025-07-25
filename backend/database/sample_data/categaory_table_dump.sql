-- SQL dump to insert initial category types
INSERT INTO category_types (id, name, is_active) VALUES
(1, 'Income', 1),
(2, 'Expense', 1),
(3, 'Savings', 1),
(4, 'Investment', 1),
(5, 'Other', 1),
(6, 'Unknown', 1),
(7, 'Asset', 1),
(8, 'Liability', 1),
(9, 'Loan', 1),
(10, 'Transfer', 1),
(11, 'Timebound', 1),
(12, 'Recurring', 1);


-- Income Categories
INSERT INTO categories (id, name, description, type_id, is_active) VALUES
(1, 'Salary', 'Monthly salary from employer', 1, 1),
(2, 'Freelance', 'Freelance or gig-based income', 1, 2),
(3, 'Bonus', 'Work-related performance bonus', 1, 2),
-- Expense Categories
(4, 'Utilities', 'Electricity, water, gas, internet bills', 2, 1),
(5, 'Transportation', 'Car, public transport, taxi expenses', 2, 1),
(6, 'Food', 'Groceries, dining out, snacks', 2, 1),
(7, 'Clothing', 'Clothing, shoes, accessories', 2, 1),
(8, 'Health', 'Medical expenses, insurance', 2, 1),
(9, 'Entertainment', 'Movies, concerts, gaming', 2, 1),
(10, 'Travel', 'Airfare, hotel, transportation', 2, 1),
(11, 'Education', 'Tuition fees, books, supplies', 2, 1),
(12, 'Personal Care', 'Haircuts, beauty products, grooming', 2, 1),
-- Savings Categories
(5, 'Savings Account', 'Bank savings account', 3, 1),
(6, 'Emergency Fund', 'Emergency fund savings', 3, 1),
(7, 'Retirement Fund', 'Retirement savings', 3, 1),
-- Investment Categories
(6, 'Stocks', 'Investment in stock market', 4, 1),
(7, 'Mutual Funds', 'Investment in mutual funds', 4, 1),
(8, 'Real Estate', 'Investment in real estate', 4, 1),
(9, 'Cryptocurrency', 'Investment in cryptocurrencies', 4, 1),
(10, 'Private Equity', 'Investment in private equity', 4, 2),
(11, 'Venture Capital', 'Investment in venture capital', 4, 2),
-- Timebound Categories
(8, 'Annual Subscription', 'Yearly subscription services', 10, 1),
(9, 'Life Insurance', 'Long-term life insurance plan', 10, 1),
-- Other Categories
(10, 'Other Income', 'Other sources of income', 5, 1),
(11, 'Other Expenses', 'Other expenses', 5, 1),
-- Loans Category
(12, 'Personal Loans', 'Personal Loan payments', 9, 1),
(13, 'Car Loans', 'Car Loan payments', 9, 1),
(14, 'Student Loans', 'Student Loan payments', 9, 1),
(15, 'Mortgage Loans', 'Mortgage Loan payments', 9, 1),
(16, 'Credit Card Payments', 'Credit Card payments', 9, 1),
(17, 'Home Loans', 'Home Loan payments', 9, 1),
(18, 'Other Loans', 'Other Loan payments', 9, 1),
-- Timebound Categories
(19, 'Annual Subscription', 'Yearly subscription services', 11, 1),
(20, 'Monthly Subscription', 'Monthly subscription services', 11, 1),
(21, 'Quarterly Subscription', 'Quarterly subscription services', 11, 1),
(22, 'Bi-Annual Subscription', 'Bi-Annual subscription services', 11, 1),
(23, 'Weekly Subscription', 'Weekly subscription services', 11, 1),
(24, 'Daily Subscription', 'Daily subscription services', 11, 1),
-- Transfers categories
(25, 'One-Time Payment', 'One-time payment', 10, 1),
(27, 'Charity', 'Charity donations', 10, 2),
-- Liability categories
(28, 'Gifts', 'Gift expenses', 8, 1),
-- Assets Category
(29, 'House payments', 'House payments', 7, 2)


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

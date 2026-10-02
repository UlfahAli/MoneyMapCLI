MoneyMap CLI

A command-line budgeting tool that helps people with tight or variable income quickly see whether their money covers their essential and priority outgoings — without needing a spreadsheet.

The problem being solved:

Most budgeting tools on the market (Monzo, YNAB, etc.) are built for general money management. But people managing debt often need something different: a quick way to see whether their income covers their priority debts and essential living costs. The framework of the project is used by UK debt advice services like StepChange and National Debtline.

MoneyMap CLI is a lightweight, independent tool for that in-between stage. This is before or alongside seeking formal debt advice, when someone just wants clarity on where they stand.

Target Audience: 

People managing debt on a tight or variable (e.g. self-employed) income, who want a fast financial snapshot without building a spreadsheet or waiting for an advice appointment.

How it works:

1. Transactions are stored in `data/transactions.csv` with the format:

   ```
   date,description,amount,type,frequency
   ```

   `type` is either `Priority` (e.g. rent, priority debt repayments) or `Essential` (e.g. food, utilities).

2. Run the script and enter your monthly income when prompted.
3. The tool totals your priority and essential costs and tells you:
   - How much you have left over, **or**
   - Your shortfall, with a prompt to seek advice from a local debt advice centre.

```
python main.py
```

Example output

```
What is your monthly income? 2000
Total priority costs: £2145.00
Your income does not cover your priority costs.
Your shortfall is: £145.00
This means your essential bills may not be fully covered this month.
Consider increasing your income and seeking advice from your local advice centre.
```

What design decisions were made?

- Priority vs Essential, not just Priority. Debt advice centres separate essential living costs from priority debts when calculating what's left for other payments. Early versions of this tool only tracked a yes/no 'priority' flag — this was changed to a 'type' column once it became clear that users may not know the difference between the two themselves, and that distinction is essential for an accurate result.
- CSV file used over a database. Keeps the project simple, transparent, and easy for a non-technical user to edit directly.
- Friendly shortfall messaging. An early version printed a raw negative number (e.g. '-145') when income didn't cover costs. This was changed to a clear shortfall message using 'abs()', plus a direct suggestion to contact a debt advice service — because the goal isn't just to show a number, it's to point toward a next step.

Some iterations

This project was built step by step rather than planned end-to-end upfront:
- Started with reading and printing raw CSV content, before parsing it into structured data with 'csv.reader'.
- Initially summed a single 'priority' category, then split it into priority vs essential once the debt-advice framework made clear these need separate handling.
- Added the shortfall/advice messaging after testing showed a bare negative number thinking of customer first architecture and the user experience. So soft, useful messaging.

What would I do next? 

- Separate totals and messaging for essential vs priority costs, rather than combining them. This may be useful for the user.
- Basic input validation (handling non-numeric income input, malformed CSV rows).
- Optional: suggest how a surplus could be allocated toward non-priority debts in the form of a DD repayment plan. 

Why I chose this project?

Drawing on prior experience in debt, housing, and welfare advice work, I have seen an increased wait in attaining advice due to Cost of Living Crisis and NEET. Also, asking for help when it comes to debt advice can be incredibly stressful, being able to have some clarity over finances in the interim is a definite need.




# Pandas Practice Project
import pandas as pd

# Load data from a CSV file
# Update the path to your actual .csv file if needed
csv_path = r"C:\Users\munir\OneDrive\Desktop\datasets\best_selling_video_games.csv"

try:
    df = pd.read_csv(csv_path)
    """----------------------------data cleaning --------------------"""

    """
    After reviewing the dataset, the 'Rank' column was found to contain 
    non-numeric string values in some rows.
    
    Since the dataset is originally ordered from top to bottom by best rank,
    missing or invalid rank values will be replaced based on their positional 
    index within the dataset.
    
    Valid numeric ranks are preserved, while invalid entries are reassigned 
    using their row position to maintain ranking consistency.
    """
    rank_raw = df['Rank'].where(df['Rank'].notna(), '')
    rank_num = pd.to_numeric(df['Rank'], errors='coerce')
    non_int_mask = rank_num.isna() | (rank_num % 1 != 0)
    df.loc[non_int_mask, 'Title'] = (
        df.loc[non_int_mask, 'Title'].astype(str).str.strip()
        + ' '
        + rank_raw[non_int_mask].astype(str).str.strip()
    ).str.strip()
    df['Rank'] = rank_num.where(~non_int_mask, pd.NA)
    df['Rank'] = df['Rank'].fillna(pd.Series(df.index + 1, index=df.index)).astype('int64')

    """The column 'Ref.' is mostly empty values, and 'Table_Number' serves no purpose in terms of analysis, so it is best to drop them."""
    df = df.drop(columns=['Ref.', 'Table_Number'])
    
    """
Clean and standardize the 'Releaseyear' column by removing non-numeric
characters and enforcing a 4-digit year format (YYYY).

Identify invalid or misplaced year values that do not match expected
patterns (1900–2099). For these rows, swap values between 'Releaseyear'
and 'Platform(s)' to correct column misalignment, then re-clean the
'Releasyear' field to ensure consistency.

This approach preserves data integrity while correcting structural
errors caused by inconsistent source formatting.
"""
    # Standardize Releaseyear to 4-digit numeric string
    releaseyear_str = df['Releaseyear'].astype(str).str.strip()
    releaseyear_clean = (
        releaseyear_str
        .str.replace(r'[^0-9]', '', regex=True)
        .str.slice(0, 4)
    )

    df['Releaseyear'] = releaseyear_clean

    # Detect invalid year values (not 19xx or 20xx)
    invalid_releaseyear = ~df['Releaseyear'].str.match(
        r'^(19|20)\d{2}$', na=False
    )

    # Swap misaligned values between Releaseyear and Platform(s)
    swap_values = df.loc[invalid_releaseyear, 'Releaseyear']

    df.loc[invalid_releaseyear, 'Releaseyear'] = (
        df.loc[invalid_releaseyear, 'Platform(s)']
        .astype(str)
        .str.replace(r'[^0-9]', '', regex=True)
        .str.slice(0, 4)
    )

    df.loc[invalid_releaseyear, 'Platform(s)'] = swap_values

    # Final cleanup
    df['Releaseyear'] = (
        df['Releaseyear']
        .astype(str)
        .str.replace(r'[^0-9]', '', regex=True)
        .str.slice(0, 4)
    )

    """--------------------------Missing Data Handling----------------------------"""

    """sales is important if not exsisting row redeamed unvalubal
    if Sales(millions) is not an int, value is = to NaN"""
    df['Sales(millions)'] = pd.to_numeric(df['Sales(millions)'], errors='coerce')
    df = df.dropna(subset=['Sales(millions)'])
    df['Sales(millions)'] = df['Sales(millions)'].astype('int64')
   
   
    """filling missing values with 'unknown' and 'indie game',
    they are catagorical data, it is better to fill instead of empty"""
    df['Publisher(s)'] = df['Publisher(s)'].fillna('Unknown')
    df['Series'] = df['Series'].fillna('Indie Game')

    print(df.head())
    print("\nMissing values per column:")
    print(df.isna().sum())
except FileNotFoundError:
    print(f"CSV file not found at: {csv_path}")

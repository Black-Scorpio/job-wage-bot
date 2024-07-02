import pandas as pd


def load_data(file_path):
    """Load CSV data into a Pandas DataFrame."""
    return pd.read_csv(file_path)


def clean_wage_columns(df):
    """Clean and convert wage columns to numeric values."""
    wage_columns = ['Low', 'Median', 'High']
    for column in wage_columns:
        df[column] = df[column].replace('[\$,]', '', regex=True).astype(float)
    return df


def display_head(df, n=5):
    """Display the first n rows of the DataFrame."""
    return df.head(n)


def display_tail(df, n=5):
    """Display the last n rows of the DataFrame."""
    return df.tail(n)


def get_summary_statistics(df):
    """Get summary statistics of the DataFrame."""
    return df.describe()


def sort_by_column(df, column_name, ascending=True):
    """Sort the DataFrame by a specific column."""
    return df.sort_values(by=column_name, ascending=ascending)


def filter_by_occupation(df, occupation):
    """Filter the DataFrame by occupation."""
    return df[df['Occupation'].str.contains(occupation, case=False, na=False)]


def get_top_n_high_wages(df, n=10):
    """Get the top N occupations with the highest wages."""
    return df.nlargest(n, 'High')


def get_bottom_n_low_wages(df, n=10):
    """Get the bottom N occupations with the lowest wages."""
    return df.nsmallest(n, 'Low')


def save_to_csv(df, file_path):
    """Save the DataFrame to a CSV file."""
    df.to_csv(file_path, index=False)


def main():
    # Load the data
    file_path = 'example_wages.csv'  # Input actual csv file name here
    df = load_data(file_path)

    # Clean the wage columns
    df = clean_wage_columns(df)

    # Display the first few rows
    print("Head of the DataFrame:")
    print(display_head(df))

    # Display the last few rows
    print("\nTail of the DataFrame:")
    print(display_tail(df))

    # Display summary statistics
    print("\nSummary Statistics:")
    print(get_summary_statistics(df))

    # Sort by High wage column
    print("\nDataFrame sorted by High wage:")
    print(sort_by_column(df, 'High').head())

    # Filter by occupation containing "Engineer"
    print("\nFilter by occupation containing 'Engineer':")
    print(filter_by_occupation(df, 'Engineer').head())

    # Get top 10 occupations with the highest wages
    print("\nTop 10 occupations with the highest wages:")
    print(get_top_n_high_wages(df, 10))

    # Get bottom 10 occupations with the lowest wages
    print("\nBottom 10 occupations with the lowest wages:")
    print(get_bottom_n_low_wages(df, 10))

    # Save the filtered DataFrame to a new CSV file
    filtered_df = filter_by_occupation(df, 'Engineer')
    save_to_csv(filtered_df, 'filtered_wage_report.csv')


if __name__ == "__main__":
    main()

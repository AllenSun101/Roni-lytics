
def orders_in_month(df, months):
    dfMonth = df.loc[df['Sent Date'].dt.month_name().isin(months)]

    dfMonth['day'] = dfMonth['Sent Date'].dt.day
    days = dfMonth.groupby(dfMonth["day"])['Order ID'].nunique()

    return days.to_frame()



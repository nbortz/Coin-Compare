class Coin:
    def __init__(self, name, price, holder_ratio, total_impressions, seven_day_sentiment, time_to_ath):
        # coin name
        self.name = name
        # current price
        self.price = price
        # ratio of holders versus market cap
        self.holder_ratio = holder_ratio
        # total impressions
        self.total_impressions = total_impressions
        # seven day sentiment analysis from tweet binder
        self.seven_day_sentiment = seven_day_sentiment
        # time to all-time high
        self.time_to_ath = time_to_ath

    def __repr__(self):
        return (f"Coin(name={self.name}, price={self.price}, "
                f"holder_ratio={self.holder_ratio}, total_impressions={self.total_impressions}, "
                f"seven_day_sentiment={self.seven_day_sentiment}, time_to_ath={self.time_to_ath})")

    def __str__(self):
        return (f"Coin: {self.name}\n"
                f"Price: {self.price}\n"
                f"Holder to Market Cap Ratio: {self.holder_ratio}\n"
                f"Total Impressions: {self.total_impressions}\n"
                f"Seven Day Sentiment: {self.seven_day_sentiment}\n"
                f"Time to ATH: {self.time_to_ath}")

    # Comparison operators for price, can adjust later
    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

    # Comparison operators for holder_ratio, place holders, can adjust later
    def compare_holder_ratio(self, other):
        return self.holder_ratio == other.holder_ratio

# Example usage
bitcoin = Coin(
    name="Bitcoin",
    price=50000,
    holder_ratio=0.05,
    total_impressions=1000000,
    seven_day_sentiment=0.8,
    time_to_ath=8000
)

ethereum = Coin(
    name="Ethereum",
    price=4000,
    holder_ratio=0.04,
    total_impressions=800000,
    seven_day_sentiment=0.75,
    time_to_ath=9000
)

print(bitcoin > ethereum)  # Compare prices
print(bitcoin.compare_holder_ratio(ethereum))  # Compare holder ratios
print(bitcoin)

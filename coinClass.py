class Coin:
    def __init__(self, name, price, holder_ratio, big_holders, repeat_buyers, growth_week, growth_month, growth_6months):
        #coin name
        self.name = name
        #current price
        self.price = price
        #ratio of holders with over 5% market cap
        self.holder_ratio = holder_ratio
        #wallet adresses of holders with over 7%
        self.big_holders = big_holders
        #percent of buyers with more than 2 purchases in the last month
        self.repeat_buyers = repeat_buyers
        #growth rates for week, month and 6 months
        self.growth_week = growth_week
        self.growth_month = growth_month
        self.growth_6months = growth_6months

    def __repr__(self):
        return (f"Coin(name={self.name}, price={self.price}, "
                f"holder_ratio={self.holder_ratio}, big_holders={self.big_holders}, "
                f"repeat_buyers={self.repeat_buyers}, growth_week={self.growth_week}, "
                f"growth_month={self.growth_month}, growth_6months={self.growth_6months})")

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

    def compare_big_holders(self, other):
        return self.big_holders == other.big_holders

    def compare_repeat_buyers(self, other):
        return self.repeat_buyers == other.repeat_buyers

    def compare_growth_week(self, other):
        return self.growth_week == other.growth_week

    def compare_growth_month(self, other):
        return self.growth_month == other.growth_month

    def compare_growth_6months(self, other):
        return self.growth_6months == other.growth_6months

# Example usage
bitcoin = Coin(
    name="Bitcoin",
    price=50000,
    holder_ratio=0.05,
    big_holders=10,
    repeat_buyers=5000,
    growth_week=0.02,
    growth_month=0.05,
    growth_6months=0.1
)

ethereum = Coin(
    name="Ethereum",
    price=4000,
    holder_ratio=0.04,
    big_holders=8,
    repeat_buyers=3000,
    growth_week=0.03,
    growth_month=0.06,
    growth_6months=0.12
)

print(bitcoin > ethereum)  # Compare prices
print(bitcoin.compare_holder_ratio(ethereum))  # Compare holder ratios

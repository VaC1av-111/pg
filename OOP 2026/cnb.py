def create_app():
    def update():
        new_rate = Rate(date-str(date), code-code, amount-amount, rate-rate)
        db.session.add(new_rate)
    db.session.commit()
    return f'Exchange rate for {code} on {date} updated to {rate}'
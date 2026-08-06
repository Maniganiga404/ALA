# ALA
class UpiId:
  def __init__(self, id, bank_id):
    self.my_id = id
    self.my_bank_id = bank_id

  def __repr__(self):
    return "upi" + self.my_id + "@" + self.my_bank_id
  def __eq__(self, other):
    return self.my_id == other.my_id and self.my_bank_id == other.my_bank_id

mani_upi_id = UpiId("9606797891", "okaxis")
mani_upi_id

print(mani_upi_id)

somebody = mani_upi_id
print(somebody)

somebody is mani_upi_id

somebody == mani_upi_id

other_upi_id = UpiId("9606797891", "okaxis")
other_upi_id

mani_upi_id == other_upi_id
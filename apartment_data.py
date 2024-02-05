from dataclasses import dataclass

@dataclass
class ApartmentData:
    unit_number: str
    layout_name: str
    cost: str
    unit_details: str
    availability: str

    def print_all_data(self):
        print(f'{self.unit_number} | {self.layout_name} | {self.cost} | {self.unit_details} | {self.availability}')

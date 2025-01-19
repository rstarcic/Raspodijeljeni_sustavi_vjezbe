from pydantic import BaseModel
from datetime import datetime

class CCTV_frame(BaseModel):
    id: int
    vrijeme_snimanja: datetime
    koordinate: tuple[float, float] = (0.0, 0.0)
    
    def __str__(self):
        formatted_datetime = self.vrijeme_snimanja.strftime('%Y-%m-%dT%H:%M:%S')
        return f"id={self.id} vrijeme_snimanja={formatted_datetime} koordinate={self.koordinate}"

cctv = CCTV_frame(id=2, vrijeme_snimanja=datetime.now(), koordinate=(12.34, 23.67))
print(cctv)

cctv_bez_koordinata = CCTV_frame(id=4, vrijeme_snimanja=datetime.now())
print(cctv_bez_koordinata)
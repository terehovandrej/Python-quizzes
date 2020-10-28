

import re
"С227НА777 КУ22777 Т22В7477 М227К19У9 С227НА777"
input = 'С227НА77'
pattern_private = r"[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}"
pattern_taxi = r"[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}"

if re.findall(pattern_private, input):
   print("Private")
elif re.findall(pattern_taxi, input):
    print("Taxi")
else:
    print("Fail")

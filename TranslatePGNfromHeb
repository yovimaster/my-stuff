# coding: utf-8
import time 
import re
from string import maketrans

nummap = {ord(c): ord(t) for c, t in zip(u"אבגדהוזחצפרךמ",u"abcdefghRNBQK")}

f = open('PGN.txt', 'w') 
pgnQ = (u'1. פג3 פג6 2. ח3 ה5 3. ה4 ד6 4. רב5 פו6 5. פו3 א6 6. ר:ג6+ ב:ג6 7. ד4 ג5 8. ד:ה5 ד:ה5 9. מה:ד8+ מ:ד8 10. פ:ה5 פד7 11. פ:ו7+ מה8 12. פ:ח8 פה5 13. א4 פג4 14. ח4 רה6 15. ז3 צד8 16. צז1 רד6 17. רז5 רה7 18. מו1 ר:ז5 19. ח:ז5 פד2+ 20. מז2 מד7 21. צזד1 מה8 22. מח2 פג4 23. צא2 פה3 24. צ:ד8+ מ:ד8 25. צא1 פ:ג2 26. צג1 רב3 27. ה5 ג4 28. מז2 פב4 29. א5 פד3 30. צח1 פ:ב2 31. צ:ח7 רג2 32. צח4 פד1 33. צד4+ מה7 34. מח2 פ:ג3 35. צ:ג4 פה2 36. צ:ג7+ מה6 37. צ:ג2 פד4 38. צג5 פה2 39. מח3 ')

l = re.sub(u'\u05de\u05d4([1-9])',r'Ke\1',pgnQ)




l = l.replace(u'\u05de\u05d4',u'ך')
l = l.replace(u':',u'x')

print l.translate(nummap)

f.write(l.translate(nummap))


f.close()

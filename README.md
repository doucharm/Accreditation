# Accreditation
 Naplnění dat o akreditaci Využijte zdroje dat pro získání informací o akreditacích (GQL_Granting). Vytvořte JSON datovou strukturu (kompatibilní se systemdata.json). Vytvořte program, který importuje data do GQL endpointů (s využitím mutací). Zabezpečte existenci propojení (ExternalIDs) se zdrojovým IS
<br/> Potřebná data pro vygenerování
 <ol>
  <li>acsemesters</li>
  <li>acsubjects</li>
  <li>acprograms</li>
  <li>groups</li>
  <li>memberships</li>
  <li>acprograms_students</li>
 </ol>
Postup
<ol>
 <li>Sbírat a třídit studenty do studijních skupin</li>
 <li>Získat informace o program=>subjekt=>semeseter pro každou skupinu</li>
 <li>Vygenerovat skutečné klasifikace</li>
 <li>Výsledek vyčístit duplikaci a doplňit</li>
</ol>
 <br/>  Produkt
![image](https://github.com/doucharm/Accreditation/assets/115186767/1205bd00-d83d-4563-99c6-80b45fa42198)

 

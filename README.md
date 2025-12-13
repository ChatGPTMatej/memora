# Memora – když technologie pomáhá vzpomínkám zůstat naživu

Memora je aplikace, která vzniká z jednoduché, ale silné myšlenky: **pomoci lidem, kteří ztrácejí vzpomínky, znovu se orientovat ve světě kolem sebe**. Nejde o náhradu lidské péče ani lékařské léčby, ale o chytrý digitální nástroj, který pacientovi poskytuje oporu ve chvílích, kdy jeho paměť selhává. Projekt je vyvíjen dvěma vývojáři jako maturitní práce a je zaměřen především na osoby s demencí a Alzheimerovou chorobou, s potenciálním využitím v domovech důchodců a pečovatelských zařízeních.

---

## Digitální paměť spravovaná lidmi, na kterých záleží

Základem Memory je přehledná aplikace, do které lékař nebo blízký příbuzný ukládá informace o lidech z pacientova okolí. Nejde pouze o jméno a fotografii, ale o celý kontext vztahu – kdo daná osoba je, jaký má vztah k pacientovi, kdy proběhla poslední návštěva a o čem se spolu naposledy bavili. Tyto informace fungují jako externí paměť, která pomáhá pacientovi lépe chápat situace, ve kterých by se jinak cítil nejistě nebo zmateně.

Aplikace je navržena tak, aby byla snadno ovladatelná i pro netechnické uživatele. Správa profilů je rychlá a přehledná, což umožňuje udržovat data aktuální bez zbytečné administrativní zátěže. Důraz je kladen na lidský přístup a praktičnost v každodenním používání.

---

## Umělá inteligence a rozšířená realita v každodenním kontaktu

Memora využívá umělou inteligenci k rozpoznávání obličejů osob uložených v databázi. Na základě fotografie se systém učí identifikovat konkrétní lidi a propojuje je s jejich profily. Cílem není stoprocentní technická přesnost, ale funkční a spolehlivá pomoc v běžných sociálních situacích.

Plánovaným rozšířením je integrace s AR brýlemi, které pacientovi zobrazí informace přímo v jeho zorném poli. Při pohledu na rozpoznaného člověka se vedle jeho hlavy objeví plovoucí informační okno se jménem, vztahem k pacientovi a dalšími klíčovými údaji. Okno se přirozeně pohybuje spolu s osobou a nenarušuje samotnou komunikaci.

---

## Technické řešení a architektura aplikace

Aplikace je vyvíjena dvěma vývojáři a je rozdělena na frontendovou, backendovou a AI část. Frontend je postaven v **React Native**, což umožňuje provoz aplikace jak na mobilních zařízeních, tak ve webovém prostředí z jednoho společného kódu. Uživatelské rozhraní je navrženo s důrazem na jednoduchost a přehlednost.

Backend je realizován v **Pythonu pomocí frameworku Django**, který zajišťuje API, správu uživatelů a práci s daty. Pro ukládání dat je použita **PostgreSQL** databáze, která nabízí stabilní a strukturované řešení vhodné pro práci s citlivými informacemi. Umělá inteligence pro rozpoznávání obličejů je trénována samostatně v Pythonu a s backendem komunikuje přes definované rozhraní.

Memora je koncipována jako funkční prototyp vhodný pro studentský projekt, s důrazem na reálné využití a možnost budoucího rozšiřování. Architektura aplikace umožňuje další vývoj, například rozšíření AI modelu, integraci nových zařízení nebo nasazení v reálném zdravotnickém prostředí.
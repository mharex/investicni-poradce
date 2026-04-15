import streamlit as st, matplotlib.pyplot as plt


# NASTAVENÍ STRÁNKY (Titulek v prohlížeči a ikona)
st.set_page_config(page_title="Investiční automatizovaný poradce", page_icon=":chart_with_upwards_trend:", layout="wide")

# --- ÚVODNÍ SEKCE ---
st.title("📊 Nechte to na Robo poradci!")
st.subheader("Nechte automatizaci, ať udělá to nejtěžší za vás. Po zodpovězení na několik otázek obdržíte personalisované portfolio, které jde naproti vašim investičním cílům.")
st.write("Odpovězte, prosím, upřímně na následujících 20 otázek. Na základě vašich odpovědí se pokusím doporučit vhodnou strategii.")

st.divider()

# --- DEFINICE OTÁZEK A BODOVÁNÍ (Seznam slovníků) ---
# Každá otázka má text, možnosti a body pro každou možnost.
# Body: 1 = Konzervativní, 2 = Vyvážený, 3 = Dynamický
questions_data = [
    {
        "question": "1. Jaký je váš hlavní cíl investování?",
        "options": ["Ochrana peněz před inflací", "Dlouhodobé budování majetku", "Rychlý zisk i za cenu rizika"],
        "points": [1, 2, 3]
    },
    {
        "question": "2. Jak dlouho plánujete nechat peníze investované (investiční horizont)?",
        "options": ["Méně než 3 roky", "3 až 10 let", "Více než 10 let"],
        "points": [1, 2, 3]
    },
    {
        "question": "3. Jak byste popsal(a) své znalosti o investování?",
        "options": ["Jsem úplný začátečník", "Mám základní přehled (vím, co je akcie/dluhopis)", "Jsem zkušený investor"],
        "points": [1, 2, 3]
    },
    {
        "question": "4. Představte si, že vaše investice klesne o 20 % za jeden měsíc. Co uděláte?",
        "options": ["Všechno okamžitě prodám", "Nic neudělám a počkám", "Využiji poklesu a přikoupím"],
        "points": [1, 2, 3]
    },
    {
        "question": "5. Jaký je váš postoj k riziku?",
        "options": ["Chci mít jistotu, nesnáším ztráty", "Jsem ochoten/a přijmout mírné kolísání pro vyšší výnos", "Vyhledávám riziko pro možnost vysokého zisku"],
        "points": [1, 2, 3]
    },
    {
        "question": "6. Jak velkou část svých úspor chcete investovat?",
        "options": ["Méně než 10 %", "10 až 30 %", "Více než 30 %"],
        "points": [1, 2, 3]
    },
    {
        "question": "7. Jaký je váš věk?",
        "options": ["Více než 55 let", "35 až 55 let", "Méně než 35 let"],
        "points": [1, 2, 3]
    },
    {
        "question": "8. Kdybyste si měl(a) vybrat mezi jistým výnosem 3 % a možným (ale nejistým) výnosem 15 %, co zvolíte?",
        "options": ["Jistých 3 %", "Raději 3 %, ale možná bych zkusil(a) část do 15 %", "Jednoznačně možných 15 %"],
        "points": [1, 2, 3]
    },
    {
        "question": "9. Co je pro vás u investice nejdůležitější?",
        "options": ["Bezpečí (nepřijít o peníze)", "Vyváženost (rozumný výnos a rozumné riziko)", "Maximální výnos"],
        "points": [1, 2, 3]
    },
    {
        "question": "10. Jak často plánujete sledovat vývoj svých investic?",
        "options": ["Denně (a stresovat se pohyby)", "Párkrát do měsíce", "Jednou za měsíc nebo vůbec"],
        "points": [1, 2, 3]
    },
    {
        "question": "11. Máte vytvořenou dostatečnou finanční rezervu (např. 3-6 měsíčních výdajů)?",
        "options": ["Ne, nemám žádnou rezervu", "Ano, mám malou rezervu", "Ano, mám dostatečnou rezervu"],
        "points": [1, 2, 3]
    },
    {
        "question": "12. Jak byste reagoval(a), kdyby vaše investice rok po sobě stagnovala (nevydělávala)?",
        "options": ["Hledal(a) bych jiný, bezpečnější produkt", "Byl(a) bych trpělivý/á", "Přikoupil(a) bych víc, protože je to 'levné'"],
        "points": [1, 2, 3]
    },
    {
        "question": "13. Kdy budete investované peníze s největší pravděpodobností potřebovat vybrat?",
        "options": ["Do 3 let", "Po 5 letch", "Po více než 10 letech"],
        "points": [3, 2, 1]
    },
    {
        "question": "14. Jaký je váš primární zdroj příjmů?",
        "options": ["Důchod / Sociální dávky / Nestabilní brigády", "Stabilní zaměstnání", "Vlastní podnikání / Pasivní příjmy"],
        "points": [1, 2, 3]
    },
    {
        "question": "15. Co byste udělal(a) s nečekaným dědictvím 100 000 Kč?",
        "options": ["Dal(a) bych je na spořicí účet", "Rozdělil(a) bych je mezi dluhopisy a indexové fondy", "Koupil(a) bych jednotlivé akcie nebo Bitcoin"],
        "points": [1, 2, 3]
    },
    {
        "question": "16. Jak moc vás ovlivňují zprávy v médiích o krachu na burze?",
        "options": ["Velmi, mám strach o své peníze", "Čtu je, ale nepanikařím", "Ignoruji je nebo je beru jako příležitost"],
        "points": [1, 2, 3]
    },
    {
        "question": "17. Jste ochoten/a investovat do produktů bez garance vrácení vložené částky?",
        "options": ["Ne, nikdy", "Ano, ale jen u části peněz", "Ano, u většiny peněz"],
        "points": [1, 2, 3]
    },
    {
        "question": "18. Jaký je váš cíl ročního výnosu (o očištění o inflaci)?",
        "options": ["1-3 % (hlavně pokrýt inflaci)", "4-7 % (rozumný růst)", "Více než 8 % (agresivní růst)"],
        "points": [1, 2, 3]
    },
    {
        "question": "19. Rozumíte pojmu 'diverzifikace'?",
        "options": ["Ne, nevím, co to je", "Ano, vím, že nemám sázet vše na jednu kartu", "Ano, aktivně diverzifikuji napříč aktivy i regiony"],
        "points": [1, 2, 3]
    },
    {
        "question": "20. Co byste udělal(a), kdyby váš známý vydělal na jedné akcii 100 % za týden?",
        "options": ["Pogratuluji mu, ale sám/sama takto neriskuji", "Zkusím zjistit víc a možná investuji malou část", "Hned tu akcii koupím taky"],
        "points": [1, 2, 3]
    }
]

# --- ZOBRAZENÍ OTÁZEK A SBĚR ODPOVĚDÍ ---
# Budeme ukládat indexy vybraných odpovědí
user_answers = []

st.header("📋 Dotazník")
st.write("Vyberte prosím jednu odpověď u každé otázky:")

# Procházíme data a vytváříme st.radio pro každou otázku
for i, item in enumerate(questions_data):
    # Klíč musí být unikátní, používáme index
    answer_idx = st.radio(item["question"], item["options"], key=f"q_{i}", index=None)
    user_answers.append(answer_idx)
    st.write("---") # Oddělovač pro přehlednost

# --- TLAČÍTKO PRO VYHODNOCENÍ ---
st.divider()
if st.button("📈 Zjistit můj investiční profil", type="primary"):
    
    # Kontrola, zda uživatel odpověděl na všechny otázky
    if None in user_answers:
        st.error("⚠️ Prosím, odpovězte na všechny otázky před vyhodnocením.")
    else:
        # Výpočet celkového skóre
        total_score = 0
        for i, answered_option in enumerate(user_answers):
            # Zjistíme index vybrané možnosti v seznamu options
            option_index = questions_data[i]["options"].index(answered_option)
            # Přičteme odpovídající body
            total_score += questions_data[i]["points"][option_index]
            
        # Zobrazení výsledku
        st.divider()
        st.header(f"Výsledek: Vaše skóre je {total_score} bodů")
        
        # Minimální skóre je 20 (vše za 1 bod), maximální 60 (vše za 3 body).
        
        # LOGIKA PRO ROZŘAZENÍ DO SKUPIN
        if total_score <= 30:
            st.success("🧱 Tvůj profil: Defenzivní investor")
            st.subheader("Charakteristika:")
            st.write("Vaší prioritou je bezpečí a ochrana kapitálu. Nesnášíte propady na trzích a jste ochoten/a přijmout nižší výnos a jste smířeni s tím, že váš výnos nemusí ani pokrýt inflaci.")
            st.subheader("Doporučené rozložení aktiv:")
            st.info("- 70 % Spořicí účty, stavební a penzijní spoření\n- 20 % Konzervativní podílové fondy (dluhopisové)\n- 10 % Jednotlivé akcie")
            labels = ['Spořicí účty', 'Konzervativní podílové fondy (dluhopisy)', 'Jednotlivé akcie']
            sizes = [70, 20, 10]
            colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

            fig, ax = plt.subplots()
            fig, ax = plt.subplots(figsize=(4, 3))
            fig.patch.set_alpha(0.0)
            ax.patch.set_alpha(0.0)
            wedges, texts, autotexts = ax.pie(
                sizes, 
                labels=labels, 
                autopct='%1.1f%%', 
                startangle=90, 
                colors=colors
            )
            for text in texts:
                text.set_color('white')
            ax.axis('equal') #kulatý
            st.write("### Doporučená struktura portfolia")
            st.pyplot(fig)

        elif total_score <= 40:
            st.warning("⚖️ Tvůj profil: Opatrný investor")
            st.subheader("Charakteristika:")
            st.write("Hledáte kompromis mezi výnosem a rizikem. Rozumíte tomu, že běžný účet vám zhodnocení nepřinese, ale stále preferujete nižší výnos s větší jistotou..")
            st.subheader("Doporučené rozložení aktiv:")
            st.info("- 50 % Indexová ETF (např. S&P 500, MSCI World)\n- 30 % Dluhopisy\n- 15 % Nemovitosti (fondy nebo fyzické)\n- 5 % Kryptoměny")
            labels = ['Akcie', 'Dluhopisy', 'Nemovitosti', 'Kryptoměny']
            sizes = [50, 30, 15,5]
            colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

            fig, ax = plt.subplots()
            fig, ax = plt.subplots(figsize=(4, 3))
            fig.patch.set_alpha(0.0)
            ax.patch.set_alpha(0.0)
            wedges, texts, autotexts = ax.pie(
                sizes, 
                labels=labels, 
                autopct='%1.1f%%', 
                startangle=90, 
                colors=colors
            )
            for text in texts:
                text.set_color('white')
            ax.axis('equal') #kulatý
            st.write("### Doporučená struktura portfolia")
            st.pyplot(fig)

        elif total_score <= 50:
            st.warning("📊Tvůj profil: Vyvážený investor")
            st.subheader("Charakteristika:")
            st.write("Jste si plně vědomi vztahu mezi rizikem a výnosem, jste ochotni podstoupit střední míru rizika a akceptovat krátkodobé propady trhů, protože víte, že historicky rostou.")
            st.subheader("Doporučené rozložení aktiv:")
            st.info("- 60% Akcie a ETF (Apple, Google, S&P 500,MSCI World )\n - 30% Dluhopisy\n 10% Spořicí účty, stavební a penzijní spoření")
            labels = ['Akcie a ETF', 'Dluhopisy', 'Spořicí účty, stavební a penzijní spoření']
            sizes = [60, 30, 10] # Procenta, musí dát dohromady 100
            colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
                # TVORBA GRAFU (Matplotlib)
            fig, ax = plt.subplots()
            fig, ax = plt.subplots(figsize=(4, 3))
            fig.patch.set_alpha(0.0)
            ax.patch.set_alpha(0.0)

            wedges, texts, autotexts = ax.pie(
                sizes, 
                labels=labels, 
                autopct='%1.1f%%', 
                startangle=90, 
                colors=colors
            )
            for text in texts:
                text.set_color('white')
            ax.axis('equal')  # Zajistí, že koláč bude kulatý
                
                # ZOBRAZENÍ VE STREAMLITU
            st.write("### Doporučená struktura portfolia")
            st.pyplot(fig)

        else:
            st.error("🚀 Tvůj profil: Dynamický (Růstový) investor")
            st.subheader("Charakteristika:")
            st.write("Cílíte na maximální dlouhodobý výnos a počítáte s vysokým rizikem. Výrazné propady na trzích vás nerozhodí, naopak je berete jako příležitost k nákupu.")
            st.subheader("Doporučené rozloženi aktiv:")
            st.info("- 70 % Akcie (jednotlivé tituly, růstová ETF, rozvíjející se trhy)\n- 15 % Kryptoměny (širší portfolio)\n- 10 % Komodity / Alternativní investice")
            labels = ['Akcie', 'Kryptoměny', 'Komodity / Alternativní investice']
            sizes = [70, 20, 10]
            colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

            fig, ax = plt.subplots()
            fig, ax = plt.subplots(figsize=(4, 3))
            fig.patch.set_alpha(0.0)
            ax.patch.set_alpha(0.0)
            wedges, texts, autotexts = ax.pie(
                sizes, 
                labels=labels, 
                autopct='%1.1f%%', 
                startangle=90, 
                colors=colors
            )
            for text in texts:
                text.set_color('white')
            ax.axis('equal') #kulatý
            st.write("### Doporučená struktura portfolia")
            st.pyplot(fig)

# --- PATIČKA ---
st.divider()
st.caption("Upozornění: Tento nástroj slouží pouze pro vzdělávací a demonstrační účely v rámci seminární práce. Nejedná se o investiční poradenství.")

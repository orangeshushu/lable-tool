# Covert clean data csv format into html
import os
import csv
import numpy as np
# Here is the folder path
filepath=".\clean_data"
namelist = os.listdir(filepath)

tag = """"""
mid_content = """"""
for username in namelist:
    username_path = filepath + "\\" + username
    with open(username_path, "r", encoding="UTF-8") as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        # Ignore the file when content amount less 4 rows
        if len(rows)<4:
            continue
        print("NoW is :" + username)
        res = []
        for row_content in rows[4:]:
            res.append(row_content)
        mid_content = """"""
        for row_content in res:
            # When it is a tag row
            # if np.size(row_content) == 1:
            #     tag = """"""
            #     tag = row_content[0]
            #     print(tag)
            #     # below is the tag content
            #     tag_content ="""<tr class="tbContext">
            #     <td></td>
            #     <td><span style="color: red; font-size: 35px; ">{tag_name}</span></td>
            #     <td></td>
            #     <td></td>
            #     <td></td>
            #     <td><input type="checkbox" name= \"""".format(tag_name=tag) + tag + """\"  style="width:35px; height:35px"></td>
            # </tr>"""
            #     mid_content += tag_content
            # else:
                # It is not tag content, highlight keywords in three map ways
                # keyword_highlight = row_content[1].replace(tag, """<span style="color: yellow;">{con}</span>""".format(con=tag))
                # keyword_highlight = keyword_highlight.replace(tag.upper(), """<span style="color: yellow;">{con}</span>""".format(con=tag.upper()))
                # keyword_highlight = keyword_highlight.replace(tag.lower(), """<span style="color: yellow;">{con}</span>""".format(con=tag.lower()))
                # keyword_highlight = keyword_highlight.replace(tag.capitalize(), """<span style="color: yellow;">{con}</span>""".format(con=tag.capitalize()))
                # If there is no any changes after mapping method, finding the first keyword in sentences
                # if keyword_highlight == row_content[1]:
                #     # print(row_content[1])
                #     highlight_content = """<span style="color: yellow;">{con}</span>""".format(con = keyword_highlight[row_content[1].upper().index(tag.upper()):row_content[1].upper().index(tag.upper()) + len(tag)])
                #     keyword_highlight =keyword_highlight[:row_content[1].upper().index(tag.upper())] + highlight_content + keyword_highlight[row_content[1].upper().index(tag.upper()) + len(tag):]
                # Untag tweet content
                tweet_content = """<tr class="tbContext">
                <td>{tweet_time}</td>
                <td class ="content_left">{tweet_information}</td>
                <td>{retweet_count}</td>
                <td>{favorite_count}</td>
                <td><a href="{twitter_url}">原文地址</a></td>
                <td></td>
            </tr>""".format(tweet_time = row_content[0], tweet_information = row_content[1], retweet_count = row_content[2], favorite_count = row_content[3], twitter_url = row_content[4])
                mid_content += tweet_content
        # Here is html format frame
        content = """<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>"""+username+"""</title>
</head>
<style>
    body {
        background: #000;
    }
    #Main {
        width: 2500px;
        text-align: center;
        margin: 0 auto;
    }
    table {
        width: 2500px;
        border-collapse: collapse;
        text-align: left;
        margin: 10px 5px 5px 10px;
        cursor: default;
        border: 1px solid #ccc;
        margin-top:20px;
        box-shadow: 0px 0px 10px rgba(0,255,255,0.75);
        border: 1px solid rgba(127,255,255,0.75);
        -webkit-box-shadow: 0px 0px 8px rgba(0,255,255,0.75);
        -moz-box-shadow: 0px 0px 8px rgba(0,255,255,0.75);
        box-shadow: 0px 0px 8px rgba(0,255,255,0.75);
    }
    .tbTitle>th {
        font-weight: 300;
        text-align: center;
        padding: 10px 0 10px 0;
        font: 15px "微软雅黑", Arial, Helvetica, sans-serif;
        background-color: rgba(0,93,93,0.8);
        color: rgba(127,255,255,0.75);
        text-shadow: 0px 0px 20px rgba(127,255,255,1);
    }
    th, td {
        border: 3px solid rgba(127,255,255,0.55);
        text-align: center;
        color: rgba(127,255,255,0.75);
        text-shadow: 0px 0px 20px rgba(127,255,255,1);

    }
    .tbContext:hover {
        background-color: rgba(0,99,99,0.9) !important;
    }
    td,td>a {
        font: 30px "微软雅黑", Arial, Helvetica, sans-serif;
        text-align: center;
        padding-top: 10px;
        padding-right: 10px;
        padding-left: 10px;
        padding-bottom: 10px;
        color: rgba(127,255,255,0.75);
        text-shadow: 0px 0px 20px rgba(0,255,255,0.75);
    }
    .tbContext:nth-child(2n 1) {
        background-color: rgba(0,127,127,0.1);
    }
    .content_left{
        text-align: left;
    }
</style>
<body>

<script>
    function exportCsv(obj){
        //title ["","",""]
        var title = obj.title;
        //titleForKey ["","",""]
        var titleForKey = obj.titleForKey;
        var data = obj.data;
        var str = [];
        str.push(obj.title.join(",")+"\\n");
        for(var i=0;i<data.length;i++){
            var temp = [];
            for(var j=0;j<titleForKey.length;j++){
                temp.push(data[i][titleForKey[j]]);
            }
            str.push(temp.join(",")+"\\n");
        }
        var uri = 'data:text/csv;charset=utf-8,' + encodeURIComponent(str.join(""));
        var downloadLink = document.createElement("a");
        downloadLink.href = uri;
        downloadLink.download = \" """ + username + """.csv\";
        document.body.appendChild(downloadLink);
        downloadLink.click();
        document.body.removeChild(downloadLink);
    }
    function validateForm() {
        var symptom_dic ={
            recover:["recover", "recovered"],
            test_positive:["test positive", "tested positive", "positive for Covid", "my test results is positive", "I was tested positive", "diagnosed with covid", "my COVID test was positive", "covid19", "covid-19"],
            underlying_disease: ["underlying disease", "migraines", "migraine", "sinusitis", "cancer", "autoimmune", "thrombocytopenic purpura", "anemia", "asthma", "emphysema", "bronchitis", "respiratory diseases", "heart disease", "diabetes", "HIV", "tonsils removed", "Tonsillectomy", "lupus", "multiple sclerosis"],
            symptoms: ["asymptomatic", "no symptoms", "some symptoms", "mild symptoms", "little symptoms"],
            fever:["febrile", "fever", "feverish", "run a fever", "have a fever", "develop a fever", "in a fever", "high fever", "mild fever", "low fever", "hyperthermia", "no fever", "degrees Fahrenheit", "temprature", "my temprature", "my temp is", "have a temperature", "has a temperature", "high body temperature", "body temperature above reference range", "body temperature above", "increased body temperature", "temperature elevated", "temperature raised", " temperature near to", " temperature up to", "temperature raised to", "fieber", "feel hot"],
            chills:["chill", "chills", "fever and chills", "chillness", "shivered", "shivering", "shiver", "shivers", "shivery", "shiveringly", "rigor", "ague", "algor", "shake", "shake all over", "shaking", "tremble", "trembled", "cold", "colder", "freeze", "freezing", "frigid"],
            repeated_shaking_with_chills:["repeated shaking with chills", "repeated shaking", "repeated chills"],
            sweating: ["sweat", "sweats", "sweating", "hidropoiesis", "Hidrosis", "Diaphoresis", "Perspiration", "perspire", "Perspire Profusely", "Started To Perspire", "perspire all over", "Perspire During Sleep"],
            Excessive_sweating :["Excessive sweating", "Profuse sweating", "Sweating profusely"],
            sneeze :["sneez", "Sneeze", "Sneezing", "Sneezes", "sternutation", "niesen", "achoo"],
            nose_running:["sniffle", "nose", "nosey", "nose running", "running nose", "runny nose", "run at the nose", "nose dripping", "my nose", "a streaming cold", "Nasal discharge", "run nose", "snoty"],
            Nasal_congestion :["Nasal congestion", "Sinus Congestion", "Stuffed-up nose", "Stuffed up nose", "stuffed nose", "rhinobyon", "nasal obstruction", "stuffiness"],
            Nosebleed:["nose bleed", "Nose bleeds", "nose bleeding", "nosebleed", "epistaxis", "hemorrhinia"],
            new_loss_of_taste_or_smell :["smell", "taste", "lost sense of smell", "lost sense of taste", "anosphrasia", "anosmia", "anodmia", "Can't smell", "smell nothing", "can't taste", "taste nothing"],
            cough:["cough", "nonproductive cough", "hacking cough", "tussiculation", "dry cough", "Persistent cough", "continuously coughs", "acute cough", "bad cough", "weeks of violent coughing", "coughing all night", "cough all day", "rough cough", "violent fit of coughing", "severe cough", "wracking cough", "nasty cough", "begma", "bex", "tussis", "tussive", "bechic"],
            Sputum_production:["Sputum production", "productive cough", "cough up some phlegm", "phlegm cough", "cough phlegm"],
            Shortness_of_breath:["respiratory symptoms", "breath", "Shortness of breath", "short breath", "polypnea", "Dyspnoea", "Dyspnea", "Breathless", "short of breath"],
            difficulty_breathing: ["Difficulty in breathing", "Difficulty breathing", "breathing difficulty", "breathe hard", "breathing hard", "breath hard", "breathing difficulties", "breathing difficult", "labored breathing", "Difficulty breath", "breath with difficulty", "breathlessness", "lose my breath", "hardly breath", "fighting for air", "not easy to breath", "breathing became painful", "breathing painful", "breath painful", "breathing problems", "trouble breathing", "respiratory trouble", "breathing trouble"],
            sore_throat:["sore throat", "throat sore", "throat pain", "pain in throat", "pain throat", "swollen sore throat", "sore swollen throat", "frog in the throat"],
            Swolllymph_nodes:["swollen lymph node", "lymph nodes", "lymph node", "swollen lymph nodes", "lymphadenopathy", "swollen neck glands", "neck glands swollen", "Cervical lymph nodes"],
            headache:["headache", "headaches", "head aches", "head ache", "head pain", "head pains", "head pounding", "pounding pain", "My head was pounding", "My head is pounding", "pounding pain in my head", "feel blood pounding hard at the back of her head", "my head to start pounding", "my head's been pounding for a good 6 hours"],
            Dizzy :["Dizzy", " dizzy spells", " dizzy spell", "Sudden dizziness", "frequent dizzy spells", " I get vertigo occasionally"],
            Muscle_pain :["Muscle pain", "muscle ace", "Muscle pains", "muscle aces"],
            body_ache:["achy all over", "don't feel well", "aching all over", "aches and pains", "body ache", "body aches", "body pain", "body pains"],
            Joint_pain:["joint pain", "joint pains", "joint ache", "joint aches", "bone pain", "bone pains", "Articular pain", "bone ache", "bone aches"],
            eye_pain:["eyes burn", "eyes pricked", "Stinging eyes", "Stinging eye", "eyes stining", "eye stining", "red eyes", "Eye fatigue", "Eyes fatigue", "red eye", "swollen eyes", "swollen eye", "sore eye", "sore eyes", "eye irritation", "itchy eyes", "itch eyes", "eyes itchy", "eye itchy", "eyeball pain", "eye ball pain", "pain in eye", "pains in eye", "pain in eyes", "pains in eyes"],
            intolerance_of_light :["intolerance of light", "photophobia", "sensitivity to light", "sensitive to light", "light sensitive", "light sensitivity"],
            hyperemia_or_chemosis:["hyperemia", "chemosis", "hyperemia or chemosis", "hyperemia chemosis"],
            eye_secretions:["eye discharge", "puffy eyes", "puffy eye", "Blurred vision", "watery eyes", "water eyes"],
            Hearing_finding:["pains in ears", "pains in ear", "pains in my ear", "pains in my ears", "ear pain", "ear aches", "ear ache", "ears pop", "ear pop", "tinnitus"],
            Sinus_pain :["Sinus pain"],
            Other_pain:["pains", "pain", "painful", "ache", "aches", "achy", "giddiness", "abdominal pain"],
            Loss_of_appetite:["poor appetite", "inappetence", "lost my appetite", "loss of appetite", "no appetite"],
            nause:["nausea", "nauseated", "nauseous", "naupathia", "nausea and vomiting"],
            vomiting:["vomit", "vomiting"],
            diarrhea:["diarrhea", "diarrhoea", "loose stool", "loose stools","chronic diarrhea"],
            Severe_diarrhoea :["Severe diarrhoea", "cacatory", "loose stool", "loose stools", "Rice water stool"],
            Lethargy: ["Lethargy", "drowsiness", "sleepiness", "excessive sleep"],
            Difficulty_sleeping:["Difficulty sleeping", "sleep difficult", "difficult sleep"],
            fatigue :["fatigue", "tired", "tiredness", "fatigued", "weary", "exhausted"],
            hallucinations:["hallucinations", "hallucination", "illusion", "illusionary", "phonism", "auditory hallucination", "visual hallucination"],
            skin:["Kawasaki like illness", "Blood clots", "red spots", "pink spots", "red spots", "brown spots", "rash", "tiny red spots on your skin like a rash", "purpura", "thrombocytopenic purpura", "blue lips", "blue face", "Bluish lips or face"],
            Itching: ["pruritus", "Itching","itch", "itchy", "itchs"],
            covid_toes :["covid toes","red toes", "toes red"],
            treatment:["doctor prescribed some medicine", "doctor prescribed some drugs", "prone", "proning"],
            heath_products:["heath products"],
            medicine:["medicine", "drug", "doctor gave me some meidicine", "doctor gave me some medication", "prescribe me some"],
            Bronchodilator: ["Bronchodilator", "inhaler", "Salbutamol", "terbutaline", "albuterol", "Ventolin", ],
            Non_opioid_analgesic:["Tylenol", "Panadol", "Excedrin", "nebs"],
            NSAID :["Ibuprofen", "Aspirin"],
            antibiotics:["Amoxicillin", "moxifloxacin", "antibiotics", "penicillin"],
            Chloroquine:["Chloroquine", "Chloroxine", "Hydroxychloroquine", "Hydroxychloroquine sulfate"],
            Vitamin:["vit", "vitmin", "Vitamin C", "Vitamin D"],
            Complementary_therapy: ["Acupressure", "acupuncture", "Aromatherapy", "Chiropraxy", "massage", "Herbal therapy", "Holistic massage therapy", "Homeopathic therapy", "Massage using Bowen technique", "Naturopathic medicine", "Osteopathy", "Probiotic therapy", "Reflexology", "Reiki", "Shiatsu", "Touch", "Traditional Chinese Medicine", "Traditional Maori medicine", "Herbal medicine agen"],
            Mineral: ["Mineral", "zinc"],
            nutritional_diet: ["nutritional diet", "vegetarians"]
        };
        res = {}
        // var symptom_dic ={
        // type:["porsche", "hello"], model:["911","888"], color:["white","red"]
        // };
        // var x = document.forms["myForm"]["check"].value;
        var lable_status = document.getElementsByTagName("input")
        // console.log(y.checked)
        for(var i = 0; i < lable_status.length; i ++){
            if(lable_status[i].checked){
                labelname = lable_status[i].name
                for(symptom_element in symptom_dic){
                    if(symptom_dic[symptom_element].indexOf(labelname) > -1){
                        res[symptom_element] = 1
                    }
                }
            }
        }
        exportCsv({
                title:['recover', 'test_positive', 'underlying_disease', 'symptoms', 'fever', 'chills', 'repeated_shaking_with_chills', 'sweating', 'Excessive_sweating', 'sneeze', 'nose_running', 'Nasal_congestion', 'Nosebleed', 'new_loss_of_taste_or_smell', 'cough', 'Sputum_production', 'Shortness_of_breath', 'difficulty_breathing', 'sore_throat', 'Swolllymph_nodes', 'headache', 'Dizzy', 'Muscle_pain', 'body_ache', 'Joint_pain', 'eye_pain', 'intolerance_of_light', 'hyperemia_or_chemosis', 'eye_secretions', 'Hearing_finding', 'Sinus_pain', 'Other_pain', 'Loss_of_appetite', 'nausea', 'vomiting', 'diarrhea', 'Severe_diarrhoea', 'Lethargy', 'Difficulty_sleeping', 'fatigue', 'hallucinations', 'skin', 'Itching', 'covid_toes', 'treatment', 'heath_products', 'medicine', 'Bronchodilator', 'Non_opioid_analgesic', 'NSAID', 'antibiotics', 'Chloroquine', 'Vitamin', 'Complementary_therapy', 'Mineral', 'nutritional_diet'],
                titleForKey:['recover', 'test_positive', 'underlying_disease', 'symptoms', 'fever', 'chills', 'repeated_shaking_with_chills', 'sweating', 'Excessive_sweating', 'sneeze', 'nose_running', 'Nasal_congestion', 'Nosebleed', 'new_loss_of_taste_or_smell', 'cough', 'Sputum_production', 'Shortness_of_breath', 'difficulty_breathing', 'sore_throat', 'Swolllymph_nodes', 'headache', 'Dizzy', 'Muscle_pain', 'body_ache', 'Joint_pain', 'eye_pain', 'intolerance_of_light', 'hyperemia_or_chemosis', 'eye_secretions', 'Hearing_finding', 'Sinus_pain', 'Other_pain', 'Loss_of_appetite', 'nausea', 'vomiting', 'diarrhea', 'Severe_diarrhoea', 'Lethargy', 'Difficulty_sleeping', 'fatigue', 'hallucinations', 'skin', 'Itching', 'covid_toes', 'treatment', 'heath_products', 'medicine', 'Bronchodilator', 'Non_opioid_analgesic', 'NSAID', 'antibiotics', 'Chloroquine', 'Vitamin', 'Complementary_therapy', 'Mineral', 'nutritional_diet'],
                data:[res]
            });
        console.log(res)
    }
</script>

<br>
<H1 style="text-align: left;"><span style="color: white; ">"""+username+""""</span></H1></body>
<br>
<div id="Demo" style="height: 67px; max-height: 989px;">
    <div id="Main">
        <form name="myForm" onsubmit="validateForm()" method="post">
            <table style="table-layout:fixed;word-break:normal;>
			<tbody>
			<tr class="tbTitle">
            <th width= "10">created_at</th>
            <th width= "54">full_text</th>
            <th width= "1">retweet_count</th>
            <th width= "1">favorite_count</th>
            <th width= "2">twitter_url</th>
            <th width="1">reslut</th>
            </tr>
            </tbody>""" + mid_content + """            
            </table>
            <br>
            <br>
            <input type="button" onclick="validateForm()" value="完成提交" style="text-align: center; width: 200px; height: 100px;font-size: 30px;background-color: lightgreen">
        </form>
    </div>
</div>
</body>
</html>"""
    # print(content)
    with open(".\html\{filename_username}.html".format(filename_username=username), "w", encoding="UTF-8") as f:
        f.write(content)

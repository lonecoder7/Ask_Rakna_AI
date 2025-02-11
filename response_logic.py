def get_healthcare_response(user_input):
    if "cough" in user_input:  
        return "Drink warm liquids such as herbal teas, honey, or lemon water, and ensure you rest your voice. Consider using a humidifier to keep the air moist, which can ease irritation. If the cough persists for more than a week or worsens, or if accompanied by other symptoms such as fever or difficulty breathing, consult a healthcare provider."
    elif "headache" in user_input:  
        return "Rest in a quiet, dark room and avoid screen time. Drink plenty of water to stay hydrated, as dehydration can sometimes trigger headaches. Applying a cold or warm compress to your forehead may also provide relief. If the headache is severe, lasts more than a couple of days, or is accompanied by nausea or visual disturbances, consult a doctor."
    elif "nausea" in user_input:  
        return "Try drinking clear fluids like water, ginger tea, or clear broths to help with nausea. Eating small, bland meals may also help, such as crackers or toast. Avoid strong smells or foods that might trigger nausea. If the symptoms persist for more than 24 hours or if they are accompanied by severe vomiting, consult a doctor."
    elif "fatigue" in user_input:  
        return "Ensure you are getting adequate sleep and rest each night. Stay hydrated, and try to avoid caffeine late in the day. Eating balanced meals that include protein, fruits, and vegetables can also help maintain energy levels. If fatigue is persistent and doesn't improve with rest, consider consulting a doctor to rule out underlying causes."
    elif "pain" in user_input:  
        return "Please identify the location of the pain (e.g., back, stomach, head) to determine the possible causes. Applying ice or heat, depending on the type of pain, may help alleviate discomfort. If the pain persists, worsens, or is accompanied by other symptoms like swelling, redness, or fever, it’s essential to consult a healthcare provider."
    elif "dizziness" in user_input:  
        return "Sit down and rest in a safe, comfortable position to prevent falls. Drink water to ensure you are not dehydrated, which can sometimes cause dizziness. If dizziness persists for an extended period, worsens, or is associated with other symptoms like fainting or severe headaches, you should consult a doctor immediately."
    elif "shortness of breath" in user_input:  
        return "Seek immediate medical attention if you experience difficulty breathing, chest pain, or wheezing, as this could be a sign of a serious condition like an asthma attack or a heart issue. If shortness of breath occurs suddenly or is severe, do not wait and seek help right away."
    elif "rash" in user_input:  
        return "Apply soothing lotions such as aloe vera or hydrocortisone cream to help alleviate itching and inflammation. Keep the affected area clean and avoid scratching. If the rash spreads, becomes painful, or is accompanied by fever or swelling, consult a doctor to determine the cause and receive appropriate treatment."
    elif "swelling" in user_input:  
        return "Rest and elevate the affected area to help reduce swelling. You may also apply an ice pack wrapped in a cloth for 15-20 minutes at a time. If swelling does not subside after a few days, worsens, or is accompanied by pain or redness, it’s essential to consult a doctor for further evaluation."
    elif "sore throat" in user_input:  
        return "Try gargling with warm salt water to soothe irritation and inflammation in your throat. Drinking warm liquids such as tea with honey or soup may also provide relief. If the sore throat persists for more than a week or is accompanied by difficulty swallowing, fever, or swollen lymph nodes, consult a doctor."
    elif "chills" in user_input:  
        return "Dress warmly and use blankets to help raise your body temperature. Stay hydrated and monitor your temperature regularly. If the chills are accompanied by a high fever, body aches, or other symptoms of infection, seek medical advice to determine the cause."
    elif "vomiting" in user_input:  
        return "Stay hydrated by sipping small amounts of water, clear liquids, or oral rehydration solutions. Rest and avoid eating heavy meals until the vomiting subsides. If vomiting continues for more than 24 hours, or if there is blood or bile in the vomit, seek medical help immediately."
    elif "diarrhea" in user_input:  
        return "Drink plenty of fluids, especially electrolyte drinks, to stay hydrated. Avoid dairy, caffeine, and high-fat foods while your digestive system recovers. If diarrhea persists for more than a couple of days, or if accompanied by blood in the stool, severe abdominal pain, or fever, consult a doctor for further evaluation."
    elif "allergies" in user_input:  
        return "Take antihistamines as directed to reduce allergy symptoms such as sneezing, itching, or nasal congestion. Avoid triggers like pollen, dust, or pet dander. If symptoms are severe or do not improve with over-the-counter medications, consult a doctor for further advice and potential treatment options."
    elif "high blood pressure" in user_input:  
        return "Monitor your blood pressure regularly at home and keep track of any changes. Follow your healthcare provider’s advice regarding diet, exercise, and any prescribed medications. If you experience symptoms like dizziness, chest pain, or shortness of breath, consult a doctor immediately."
    elif "dehydration" in user_input:  
        return "Drink water or oral rehydration solutions to replenish lost fluids and electrolytes. Avoid drinks that can dehydrate you, such as alcohol or caffeine. If symptoms such as dizziness, dry mouth, or confusion persist, seek medical attention for further evaluation."
    elif "infection" in user_input:  
        return "Consult a doctor for an appropriate treatment plan, which may include antibiotics or antiviral medications depending on the type of infection. If you experience severe symptoms such as high fever, difficulty breathing, or swollen lymph nodes, seek medical help immediately."
    elif "cold" in user_input:  
        return "Rest, drink fluids, and use over-the-counter medications to alleviate symptoms such as a stuffy nose or cough. Avoid contact with others to prevent spreading the illness. If symptoms worsen or last longer than 10 days, or if you develop a fever, consult a healthcare provider."
    elif "constipation" in user_input:  
        return "Increase your fiber intake by eating fruits, vegetables, and whole grains. Drink plenty of water and consider using over-the-counter stool softeners if needed. If constipation persists for more than a week, causes pain, or is accompanied by blood in the stool, consult a doctor."
    elif "sweating" in user_input:  
        return "Stay hydrated and wear loose, breathable clothing to reduce excessive sweating. If you experience excessive sweating without physical activity, or if it is associated with other symptoms like dizziness or a racing heart, consult a doctor for further evaluation."
    elif "itching" in user_input:  
        return "Apply soothing lotion or anti-itch cream to the affected area, such as hydrocortisone or calamine lotion. Avoid scratching, as this can worsen the irritation. If itching persists, worsens, or is accompanied by a rash or swelling, consult a doctor to determine the cause."
    elif "mood swings" in user_input:  
        return "Consider relaxation techniques such as yoga, deep breathing exercises, or mindfulness meditation to manage emotional fluctuations. Regular exercise and a balanced diet can also help stabilize mood. If mood swings are severe or interfere with daily life, consult a doctor for further advice."
    elif "insomnia" in user_input:  
        return "Practice good sleep hygiene by maintaining a consistent sleep schedule, creating a relaxing bedtime routine, and limiting screen time before bed. Avoid caffeine and heavy meals close to bedtime. If insomnia persists for several weeks or interferes with your daily activities, consult a healthcare provider."
    elif "depression" in user_input:  
        return "Seek professional help from a therapist or counselor for mental health support. Support from friends and family can also be helpful. If you experience symptoms like persistent sadness, loss of interest in activities, or thoughts of self-harm, please seek immediate help from a mental health professional."
    elif "anxiety" in user_input:  
        return "Try deep breathing exercises, mindfulness, or other relaxation techniques to manage anxiety. Regular physical activity can also help reduce stress. If anxiety is overwhelming or persistent, consult a doctor or therapist for additional support and treatment options."
    elif "memory loss" in user_input:  
        return "Consult a doctor for an evaluation to determine the cause of memory loss. It may be related to normal aging, but it can also be a sign of underlying conditions such as dementia. A healthcare provider can help assess the situation and recommend appropriate steps."
    elif "muscle cramps" in user_input:  
        return "Stretch the affected muscle and hydrate with water or electrolyte drinks. You can also apply heat or cold to relieve the pain. If cramps continue or worsen, consult a doctor to rule out underlying conditions like dehydration or electrolyte imbalances."
    elif "weight loss" in user_input:  
        return "Consult a doctor to identify the underlying causes of unexplained weight loss, as it could be a sign of a medical condition. A balanced diet and exercise regimen may help, but a healthcare provider should guide any weight changes, especially if they are rapid or unintentional."
    elif "weight gain" in user_input:  
        return "Consult a doctor to rule out any underlying health conditions, such as hypothyroidism or metabolic disorders, which may contribute to unexpected weight gain. A balanced diet and exercise plan, tailored to your needs, can also help manage weight effectively."
    elif "joint pain" in user_input:  
        return "Rest the affected joint and apply ice or heat as needed to alleviate discomfort. Over-the-counter pain relievers like ibuprofen or acetaminophen may help reduce inflammation and pain. If joint pain persists or is accompanied by swelling, redness, or stiffness, consult a doctor."
    elif "sinus congestion" in user_input:  
        return "Use a saline nasal spray or rinse to clear nasal passages and reduce congestion. Inhaling steam from a hot shower or a bowl of hot water can also provide relief. If sinus congestion lasts for more than a week or is accompanied by severe facial pain, fever, or yellow/green mucus, consult a doctor."
    elif "heartburn" in user_input:  
        return "Try over-the-counter antacids to neutralize stomach acid and relieve heartburn. Avoid large meals, spicy foods, or lying down immediately after eating. If heartburn occurs frequently or is associated with chest pain, difficulty swallowing, or nausea, consult a doctor for further evaluation."
    elif "back pain" in user_input:  
        return "Rest and apply heat or ice to the affected area to relieve pain. Avoid heavy lifting and maintain good posture. If back pain is severe, doesn't improve with rest, or is accompanied by numbness or tingling in the legs, consult a healthcare provider for further assessment."
    elif "frequent urination" in user_input:  
        return "Consult a doctor to evaluate the cause of frequent urination, as it could be related to conditions such as diabetes or urinary tract infections. If accompanied by pain or blood in the urine, seek immediate medical attention."
    elif "blurry vision" in user_input:  
        return "Consult an eye doctor to assess your vision and check for underlying conditions like refractive errors or eye diseases. If you experience sudden blurry vision, especially accompanied by pain or flashes of light, seek immediate medical attention."
    elif "dry skin" in user_input:  
        return "Use moisturizers regularly to hydrate your skin and avoid long, hot showers. A humidifier can also help restore moisture to the air in dry environments. If dry skin persists or is accompanied by redness, itching, or cracks, consult a doctor for further advice."
    elif "bruising" in user_input:  
        return "Monitor for any unusual symptoms like severe pain, swelling, or the appearance of new bruises. Applying ice during the first 24 hours after the injury can help reduce swelling. If bruising is frequent or occurs without a clear cause, consult a doctor to rule out underlying conditions."
    elif "cramps" in user_input:  
        return "Apply heat to the affected area, stretch gently, and drink water or an electrolyte drink to rehydrate. If cramps are severe or don't improve with self-care, consult a doctor for further evaluation, especially if they occur frequently."
    elif "indigestion" in user_input:  
        return "Eat smaller, more frequent meals and avoid spicy, fatty, or acidic foods. Drink water and consider taking antacids if needed. If indigestion persists or is accompanied by chest pain, nausea, or weight loss, consult a doctor."
    elif "increased thirst" in user_input:  
        return "Consult a doctor to check for underlying conditions like diabetes or dehydration. Drinking water regularly can help, but it's important to rule out any potential medical causes."
    elif "cold sores" in user_input:  
        return "Apply antiviral ointment to the affected area to help reduce symptoms. Avoid touching the cold sore to prevent spreading the virus. If cold sores are frequent or painful, consult a doctor for possible prescription treatment."
    elif "feeling faint" in user_input:  
        return "Sit down and hydrate to avoid fainting, and consult a doctor to determine the cause of frequent fainting episodes."
    elif "chest pain" in user_input:  
        return "Seek immediate medical attention, as chest pain can be a sign of serious conditions such as a heart attack or angina."
    elif "persistent cough" in user_input:  
        return "Consult a doctor if the cough lasts for more than three weeks or is accompanied by other symptoms like fever, chest pain, or shortness of breath."
    elif "dizziness" in user_input:  
        return "Sit down and rest to prevent fainting. Hydrate and consult a doctor if dizziness is persistent or accompanied by other concerning symptoms."
    elif "stomach ache" in user_input:  
         return "Rest and try drinking ginger tea or peppermint tea, both of which can help soothe your stomach. Avoid greasy or spicy foods while you're recovering. If the pain persists or worsens, or is accompanied by vomiting or fever, consult a doctor."
    elif "fever" in user_input:  
        return "Rest and drink plenty of fluids to stay hydrated. You can take over-the-counter medications like acetaminophen or ibuprofen to help reduce the fever. If the fever persists for more than three days or is very high, seek medical advice."
    elif "numbness" in user_input:  
        return "Numbness in certain areas of the body can be a sign of nerve compression or poor circulation. Rest the affected area, and if numbness persists or spreads, consult a doctor for further examination."
    elif "sweating at night" in user_input:  
        return "Night sweats can sometimes be linked to menopause or an underlying infection. Stay cool with light clothing and sheets, and monitor for other symptoms like fever or weight loss. If night sweats are persistent or unexplained, consult a healthcare provider."
    elif "hiccups" in user_input:  
        return "Try holding your breath for a few seconds, drinking a glass of water, or swallowing a spoonful of sugar to help stop the hiccups. If hiccups last longer than 48 hours, it may indicate an underlying condition, and you should see a doctor."
    elif "yellowing of skin" in user_input:  
        return "Yellowing of the skin or eyes could be a sign of jaundice, which can result from liver problems. It's important to seek medical advice right away to determine the cause and receive appropriate treatment."
    elif "frequent headaches" in user_input:  
        return "Make sure you're staying hydrated, resting well, and managing stress. If headaches are frequent or particularly severe, consider keeping a headache diary to identify triggers, and consult a doctor to explore treatment options."
    elif "shaking" in user_input:  
        return "Shaking or tremors can be caused by various factors, including low blood sugar, anxiety, or even a neurological issue. If the shaking is frequent or persistent, consult a healthcare provider for further evaluation."
    elif "itchy eyes" in user_input:  
        return "Try using over-the-counter antihistamine eye drops or saline solutions to soothe irritation. Avoid rubbing your eyes, as this can worsen the itching. If symptoms persist or worsen, consult an eye doctor."
    elif "coughing up blood" in user_input:  
        return "Coughing up blood can be a serious symptom, potentially related to infections, lung disease, or other conditions. Seek immediate medical attention if you experience this symptom."
    elif "muscle weakness" in user_input:  
        return "Muscle weakness can result from overexertion, dehydration, or underlying medical conditions. Make sure you're getting enough rest, hydration, and nutrition. If the weakness persists or is accompanied by pain, consult a doctor."
    elif "difficulty swallowing" in user_input:  
        return "Difficulty swallowing, or dysphagia, can be due to various factors, such as muscle issues, acid reflux, or throat problems. If this is a recurring issue or is accompanied by pain or weight loss, consult a healthcare provider."
    elif "hair loss" in user_input:  
        return "Hair loss can be caused by stress, hormonal changes, or nutritional deficiencies. Ensure you're eating a balanced diet rich in vitamins and minerals. If hair loss persists or is severe, consider seeing a dermatologist for further evaluation."
    elif "toothache" in user_input:  
        return "Rinse your mouth with warm salt water to help alleviate pain, and use over-the-counter pain relievers as directed. See a dentist as soon as possible if the pain persists or is accompanied by swelling."
    elif "difficulty breathing" in user_input:  
        return "If you're experiencing difficulty breathing, it’s essential to seek medical attention immediately. This could be a sign of asthma, a respiratory infection, or even a more serious condition like a heart problem."
    elif "severe bruising" in user_input:  
        return "Monitor the bruise and apply ice during the first 24 hours to reduce swelling. If bruising appears without a clear cause or is accompanied by other symptoms, such as pain or swelling, consult a healthcare provider."
    elif "chronic fatigue" in user_input:  
        return "Chronic fatigue may be caused by stress, poor diet, or sleep issues. Ensure you're eating nutritious meals, staying hydrated, and sleeping well. If the fatigue is persistent, consult a doctor for a thorough evaluation."
    elif "swollen lymph nodes" in user_input:  
        return "Swollen lymph nodes can be a sign of infection or an immune response. If they are painful, persist, or are accompanied by other symptoms like fever or night sweats, consult a doctor."
    elif "loss of appetite" in user_input:  
        return "Loss of appetite can be caused by illness, stress, or certain medications. Try eating small, nutritious meals throughout the day, and if the loss of appetite persists or is accompanied by other symptoms like weight loss, consult a doctor."
    elif "back stiffness" in user_input:  
        return "Back stiffness can be relieved with gentle stretching, warm compresses, and over-the-counter pain relievers. If the stiffness persists or worsens, consult a healthcare provider for further evaluation."
    elif "swelling in the legs" in user_input:  
        return "Swelling in the legs can be a sign of fluid retention, venous insufficiency, or other conditions. Elevating your legs and reducing salt intake can help, but if the swelling persists, consult a doctor."
    elif "abdominal pain" in user_input:  
        return "Abdominal pain can range from mild to severe and may be caused by indigestion, gas, or even a more serious condition. Try drinking warm water and resting. If the pain persists or worsens, consult a doctor."
    elif "joint swelling" in user_input:  
        return "Rest the affected joint and apply ice to reduce swelling. If the swelling is persistent or accompanied by pain, redness, or warmth, consult a doctor to rule out infection or inflammation."
    elif "heart palpitations" in user_input:  
        return "Heart palpitations can be caused by stress, anxiety, or physical exertion. Try to relax and take deep breaths. If palpitations are frequent, accompanied by chest pain, or shortness of breath, seek medical attention."
    elif "pale skin" in user_input:  
        return "Paleness can be caused by anemia, dehydration, or a lack of sleep. Ensure you’re eating well, staying hydrated, and getting enough rest. If the pale skin is accompanied by dizziness or fatigue, consult a doctor."
    elif "dry eyes" in user_input:  
        return "Use artificial tears or eye lubricants to relieve dryness. Avoid long periods in front of screens and consider using a humidifier in your home. If dryness persists or is accompanied by pain or blurred vision, consult an eye doctor."
    elif "irregular heartbeat" in user_input:  
        return "An irregular heartbeat can be a sign of an arrhythmia or other heart-related issues. If you experience dizziness, chest pain, or shortness of breath, seek immediate medical attention."
    elif "bloody stool" in user_input:  
        return "Blood in the stool can be a sign of a gastrointestinal issue, such as hemorrhoids, ulcers, or even more serious conditions like colorectal cancer. Consult a doctor immediately to evaluate the cause."
    elif "stiff neck" in user_input:  
        return "A stiff neck can be caused by muscle strain or tension. Applying heat and gently stretching may help. If the stiffness persists or is accompanied by numbness, headache, or dizziness, consult a healthcare provider."
    elif "low blood sugar" in user_input:  
        return "If you’re experiencing symptoms of low blood sugar, such as shakiness, dizziness, or sweating, consume a fast-acting sugar source, like juice or glucose tablets. If symptoms persist, consult a doctor."
    elif "ringing in ears" in user_input:  
        return "Ringing in the ears, or tinnitus, can be caused by exposure to loud noises, ear infections, or other conditions. Avoid loud environments, and if the ringing persists or worsens, consult an audiologist or ENT specialist."
    elif "nail discoloration" in user_input:  
        return "Discolored nails can indicate a fungal infection, nutritional deficiency, or other health issues. If the discoloration is persistent or accompanied by pain, seek medical advice."
    elif "bloated stomach" in user_input:  
        return "A bloated stomach can be caused by gas, overeating, or food intolerances. Try gentle exercise and drinking peppermint tea to relieve discomfort. If bloating persists or is painful, consult a doctor."
    elif "canker sores" in user_input:  
        return "Canker sores can be painful but usually heal on their own. Use mouth rinses and over-the-counter medications to ease the discomfort. If sores are recurrent or unusually large, consult a dentist."
    elif "painful urination" in user_input:  
        return "Painful urination can be a sign of a urinary tract infection (UTI). Drink plenty of water and consult a healthcare provider for a proper diagnosis and treatment."
    elif "constant yawning" in user_input:  
        return "Excessive yawning could be a sign of fatigue, boredom, or a lack of sleep. Try improving your sleep routine, and if yawning continues or is accompanied by other symptoms, consult a doctor."
    elif "rashes after eating" in user_input:  
        return "Rashes that occur after eating could be a sign of an allergy or food sensitivity. Keep track of what you eat and consult a healthcare provider to determine the cause."
    elif "frequent urination at night" in user_input:  
        return "Frequent urination at night (nocturia) can be caused by fluid intake before bedtime, diabetes, or prostate issues in men. If this persists or disrupts your sleep, consult a doctor."
    elif "persistent thirst" in user_input:  
        return "Persistent thirst can indicate dehydration, diabetes, or other health conditions. Drink water regularly and consult a doctor if the thirst is excessive or accompanied by other symptoms like frequent urination."
    elif "sore muscles" in user_input:  
        return "Sore muscles can be a result of exercise or physical activity. Rest, stretch, and apply heat or cold to ease the discomfort. If the soreness lasts longer than a few days, consult a healthcare provider."
    elif "sensitivity to light" in user_input:  
        return "Sensitivity to light can be a symptom of conditions such as migraines, eye infections, or a vitamin deficiency. If it’s persistent or severe, consult an eye doctor."
    elif "bloating after meals" in user_input:  
        return "Bloating after meals can result from overeating, indigestion, or food intolerances. Try eating smaller, more frequent meals and avoid foods that trigger bloating. If it continues, see a doctor."
    elif "hair thinning" in user_input:  
        return "Hair thinning can be caused by stress, hormones, or poor nutrition. Make sure you’re eating a balanced diet and managing stress. If the thinning is noticeable, consult a dermatologist."
    elif "feeling cold all the time" in user_input:  
        return "Constant coldness may indicate hypothyroidism, anemia, or circulation issues. Stay warm and consult a healthcare provider if the sensation persists."
    elif "excessive thirst" in user_input:  
        return "Excessive thirst could indicate dehydration or conditions like diabetes. Drink plenty of water and consult a doctor if the thirst continues or worsens."
    elif "nosebleed" in user_input:  
        return "If you have a nosebleed, pinch your nostrils together and lean forward slightly. Avoid lying down or tilting your head back. If nosebleeds are frequent or prolonged, consult an ENT specialist."
    elif "sore muscles after exercise" in user_input:  
        return "Sore muscles after exercise are common. Rest, hydrate, and apply ice or heat to ease the discomfort. If soreness is severe or doesn’t improve, consult a healthcare provider."
    elif "chronic cough" in user_input:  
        return "A chronic cough can be caused by smoking, allergies, or respiratory conditions. If the cough persists for more than three weeks, consult a doctor."
    elif "redness of the skin" in user_input:  
        return "Redness of the skin can result from irritation, allergies, or a rash. Apply soothing lotions and avoid further irritation. If the redness persists or worsens, consult a healthcare provider."
    elif "chest tightness" in user_input:  
        return "Chest tightness can be a sign of anxiety, asthma, or heart conditions. If you experience tightness along with pain, shortness of breath, or dizziness, seek immediate medical attention."
    elif "bad breath" in user_input:  
        return "Bad breath can be caused by poor oral hygiene, dry mouth, or an underlying health condition. Brush and floss regularly, and drink plenty of water. If the issue persists, consult a dentist."
    elif "muscle cramps" in user_input:  
        return "Muscle cramps can be caused by dehydration, low potassium, or overuse of muscles. Drink plenty of water, stretch gently, and consider eating foods rich in potassium like bananas. If cramps persist, consult a healthcare provider."
    elif "joint pain" in user_input:  
        return "Joint pain may result from overexertion, arthritis, or an injury. Rest the affected joint, apply ice, and try over-the-counter pain relievers. If the pain continues or worsens, consult a healthcare professional."
    elif "nausea" in user_input:  
        return "Nausea can be caused by various factors, including food poisoning, anxiety, or a stomach bug. Try drinking ginger tea or sucking on peppermint candy. If nausea persists for several days, consult a doctor."
    elif "dizziness" in user_input:  
        return "Dizziness can be caused by dehydration, low blood sugar, or inner ear issues. Ensure you are well-hydrated and have eaten enough. If dizziness is persistent, consult a healthcare provider."
    elif "sore throat" in user_input:  
        return "A sore throat is commonly caused by viral infections like the cold or flu. Gargling with warm salt water, drinking warm tea with honey, and resting can help. If symptoms persist or worsen, consult a doctor."
    elif "cold hands and feet" in user_input:  
        return "Cold hands and feet can be caused by poor circulation or low body temperature. Dress warmly and keep moving to improve blood flow. If persistent, it may be related to conditions like Raynaud's disease, so consider seeing a doctor."
    elif "chronic back pain" in user_input:  
        return "Chronic back pain can be the result of posture issues, muscle strain, or spinal problems. Practice good posture, rest, and use heat or ice. If the pain persists, consult a healthcare provider for further evaluation."
    elif "sensitivity to sound" in user_input:  
        return "Sensitivity to sound may occur with migraines, ear infections, or other conditions. Rest in a quiet, dark room, and if symptoms continue, consult an ear specialist."
    elif "tinnitus" in user_input:  
        return "Tinnitus, or ringing in the ears, can be caused by exposure to loud noises, ear infections, or other conditions. If the ringing persists, it's a good idea to consult an ENT specialist."
    elif "swollen ankles" in user_input:  
        return "Swollen ankles can be caused by prolonged standing, dehydration, or an underlying health condition like heart or kidney disease. Elevate your legs, stay hydrated, and consult a doctor if the swelling persists."
    elif "nose congestion" in user_input:  
        return "Nasal congestion can be due to allergies, a cold, or sinusitis. Use a saline spray, humidify the air, and stay hydrated. If congestion persists for weeks, consult an ENT doctor."
    elif "swollen gums" in user_input:  
        return "Swollen gums may be a sign of gingivitis, gum disease, or an infection. Brush gently, floss, and consider using a mouthwash. If swelling persists, consult a dentist."
    elif "excessive sweating" in user_input:  
        return "Excessive sweating can be caused by anxiety, menopause, or hyperhidrosis. Try wearing breathable clothing and staying cool. If it's affecting your quality of life, consult a doctor."
    elif "sore feet" in user_input:  
        return "Sore feet can result from prolonged standing, wearing ill-fitting shoes, or overuse. Try soaking your feet in warm water and massaging them. If the soreness continues, see a podiatrist."
    elif "bloody nose" in user_input:  
        return "If you're experiencing a bloody nose, pinch your nostrils and lean forward slightly. Avoid lying down. If nosebleeds are frequent or severe, consult an ENT specialist."
    elif "fatigue after meals" in user_input:  
        return "Feeling tired after meals can be due to overeating, a heavy meal, or food sensitivities. Try eating smaller meals and avoid heavy or high-sugar foods. If the fatigue continues, see a doctor."
    elif "bad digestion" in user_input:  
        return "Poor digestion can be caused by stress, overeating, or food intolerances. Eat smaller meals, avoid processed foods, and try gentle movements after eating. If the issue persists, consult a healthcare provider."
    elif "shiny skin" in user_input:  
        return "Shiny skin can result from oily skin, hormonal changes, or excessive moisture. Try using oil-free skincare products, and consider visiting a dermatologist for tailored advice."
    elif "persistent cough" in user_input:  
        return "A persistent cough can be due to allergies, asthma, or post-nasal drip. Consider seeing a doctor if your cough lasts more than three weeks, or is accompanied by fever or chest pain."
    elif "difficulty focusing" in user_input:  
        return "Difficulty focusing can be caused by stress, lack of sleep, or even dehydration. Make sure you're getting enough rest and hydration. If focusing issues persist, consult a doctor."
    elif "dry scalp" in user_input:  
        return "A dry scalp can result from dandruff, harsh hair products, or dry weather. Try using a gentle, moisturizing shampoo and conditioner. If the dryness persists, consult a dermatologist."
    elif "dry skin" in user_input:  
        return "Dry skin is often caused by cold weather, dehydration, or harsh skincare products. Moisturize regularly, drink plenty of water, and use gentle skincare products. If it doesn’t improve, consult a dermatologist."
    elif "chapped lips" in user_input:  
        return "Chapped lips can be caused by dry air, dehydration, or licking your lips too much. Use a hydrating lip balm and drink plenty of water. If chapping persists, consult a dermatologist."
    elif "weak nails" in user_input:  
        return "Weak nails can be caused by dehydration, a lack of nutrients, or frequent use of nail polish remover. Eat a balanced diet rich in vitamins, and use a strengthening nail product. If the problem persists, consult a dermatologist."
    elif "feeling dizzy when standing" in user_input:  
        return "Dizziness when standing up can be due to low blood pressure or dehydration. Try standing up slowly and drinking plenty of water. If the dizziness continues, consult a doctor "
    elif "heart attack" in user_input:
        return "A heart attack is a medical emergency. Symptoms include chest pain, shortness of breath, and pain in the arm, neck, or jaw. Call 911 immediately if you or someone else is experiencing these symptoms."
    elif "stroke" in user_input:
        return "A stroke is a medical emergency. Symptoms may include sudden numbness, confusion, difficulty speaking, or severe headache. Call 911 immediately if you suspect a stroke."
    elif "severe bleeding" in user_input:
        return "Severe bleeding can be life-threatening. Apply pressure to the wound with a clean cloth or bandage, and elevate the area if possible. Seek immediate medical help."
    elif "burns" in user_input:
        return "For burns, cool the affected area with running cold water for at least 10 minutes, then cover it with a sterile dressing. Seek emergency medical attention for severe burns or blisters."
    elif "seizure" in user_input:
        return "If someone is having a seizure, stay calm and protect them from injury. Do not try to restrain them. Call 911 if the seizure lasts more than 5 minutes or if another occurs immediately afterward."
    elif "difficulty breathing" in user_input:
        return "If you're having trouble breathing, try to remain calm. If the issue persists or worsens, seek immediate medical attention."
    elif "allergic reaction" in user_input:
        return "If someone is having a severe allergic reaction, such as difficulty breathing or swelling of the face or throat, call 911 immediately. Administer an epinephrine shot if available."
    elif "choking" in user_input:
        return "If someone is choking, encourage them to cough. If they're unable to do so, perform the Heimlich maneuver and call 911."
    elif "severe headache" in user_input:
        return "A severe headache, especially if it's sudden or accompanied by vision changes, nausea, or confusion, could be a sign of a serious condition like a stroke or aneurysm. Seek immediate medical attention."
    elif "unconsciousness" in user_input:
        return "If someone is unconscious, check their breathing and pulse. If they are not breathing, begin CPR immediately and call 911."
    elif "fracture" in user_input:
        return "If you suspect a fracture, immobilize the injured area and seek medical help. Avoid moving the injured person unless necessary."
    elif "poisoning" in user_input:
        return "If someone has ingested poison, call Poison Control or 911 immediately. Do not try to make them vomit unless instructed to do so."
    elif "drowning" in user_input:
        return "If someone is drowning, call 911 immediately. If possible, rescue them using a flotation device, and begin CPR if they are unresponsive."
    elif "severe abdominal pain" in user_input:
        return "Severe abdominal pain may indicate a serious issue, like appendicitis or a ruptured organ. Seek emergency medical help."
    elif "high fever" in user_input:
        return "A high fever (above 103°F or 39.4°C) can be dangerous. Seek medical attention if the fever is persistent or accompanied by severe headache or confusion."
    elif "broken tooth" in user_input:
        return "A broken or knocked-out tooth can be an emergency. Rinse the tooth gently with water and try to keep it moist. Visit a dentist immediately."
    elif "poison ivy" in user_input:
        return "If you've come into contact with poison ivy and develop a rash, avoid scratching, clean the area, and apply calamine lotion. If severe, seek medical attention."
    elif "eye injury" in user_input:
        return "For an eye injury, avoid rubbing the eye, and cover it with a clean cloth. Seek immediate medical attention for severe injuries."
    elif "heatstroke" in user_input:
        return "Heatstroke is a life-threatening condition. Symptoms include confusion, hot skin, and rapid heartbeat. Move to a cooler place, hydrate, and seek emergency medical attention."
    elif "hypothermia" in user_input:
        return "Hypothermia can occur in cold environments. Symptoms include shivering, confusion, and slurred speech. Seek immediate medical attention and warm the person slowly."
    elif "asthma attack" in user_input:
        return "During an asthma attack, use a rescue inhaler if available. If symptoms worsen or do not improve, seek emergency medical help."
    elif "heart palpitations" in user_input:
        return "Heart palpitations, especially when accompanied by chest pain or shortness of breath, may signal a serious heart condition. Seek emergency medical attention."
    elif "spinal injury" in user_input:
        return "If you suspect a spinal injury, avoid moving the person and keep their neck stabilized. Call 911 immediately."
    elif "slashed wound" in user_input:
        return "For a deep or slashed wound, apply pressure to stop the bleeding. Elevate the area if possible and seek immediate medical attention."
    elif "severe dehydration" in user_input:
        return "Severe dehydration can be dangerous and requires immediate medical attention. Drink fluids with electrolytes and seek emergency help."
    elif "severe allergic reaction" in user_input:
        return "A severe allergic reaction can cause difficulty breathing and swelling. Call 911 immediately if these symptoms occur."
    elif "collapsed lung" in user_input:
        return "A collapsed lung can cause sharp chest pain and difficulty breathing. Call 911 immediately for emergency treatment."
    elif "severe diarrhea" in user_input:
        return "Severe diarrhea, especially if accompanied by dehydration, blood, or high fever, requires immediate medical attention."
    elif "chemical exposure" in user_input:
        return "If someone is exposed to chemicals, move them to fresh air immediately. Rinse the affected area with water and seek medical help."
    elif "concussion" in user_input:
        return "If you suspect a concussion, monitor for symptoms like dizziness, headache, and confusion. Seek medical attention immediately."
    elif "severe vomiting" in user_input:
        return "Severe vomiting, especially if accompanied by dehydration, blood, or high fever, requires immediate medical attention."
    elif "head injury" in user_input:
        return "For a head injury, keep the person still and monitor for symptoms like confusion or loss of consciousness. Seek emergency medical help."
    elif "severe back pain" in user_input:
        return "Severe back pain, especially if it radiates to the legs or causes numbness, could be a sign of a herniated disc. Seek medical help."
    elif "stomach bleeding" in user_input:
        return "Stomach bleeding can be caused by ulcers or injuries. Seek immediate medical attention if you suspect bleeding in the stomach."
    elif "broken bone" in user_input:
        return "If you suspect a broken bone, immobilize the area and avoid putting weight on it. Seek emergency medical attention."
    elif "poisonous bite" in user_input:
        return "If bitten by a venomous snake or insect, remain calm and seek immediate medical help. Try to remember the type of bite for treatment."
    elif "severe nosebleed" in user_input:
        return "For a severe nosebleed, pinch your nostrils together and lean forward. Seek medical help if bleeding persists for more than 20 minutes."
    elif "sudden vision loss" in user_input:
        return "Sudden vision loss is a medical emergency. Call 911 immediately if you experience sudden blindness or blurry vision."
    elif "severe chest pain" in user_input:
        return "Severe chest pain, especially if accompanied by shortness of breath, sweating, or nausea, could indicate a heart attack. Call 911 immediately."
    elif "dislocated joint" in user_input:
        return "For a dislocated joint, avoid moving the affected area and seek emergency medical attention for proper treatment."
    elif "acute pain in stomach" in user_input:
        return "Acute pain in the stomach, especially if accompanied by vomiting or fever, could be a sign of a serious condition like appendicitis. Seek immediate medical help."
    elif "deep cut" in user_input:
        return "For a deep cut, apply pressure to stop the bleeding and cover it with a clean bandage. Seek emergency medical help for stitches."
    elif "hemorrhage" in user_input:
        return "A hemorrhage is a life-threatening condition. Apply pressure to the wound and seek emergency medical help immediately."
    elif "cardiac arrest" in user_input:
        return "Cardiac arrest is a medical emergency. Perform CPR immediately and call 911 for help."
    elif "poisonous food" in user_input:
        return "If you've consumed poisonous food, seek immediate medical help or contact Poison Control for guidance."
    elif "severe fatigue" in user_input:
        return "Severe fatigue, especially if sudden or unexplained, can be a sign of a serious condition like anemia. Consult a doctor immediately."
    elif "difficulty swallowing" in user_input:
        return "Difficulty swallowing, especially if it’s painful or sudden, could be a sign of an obstruction or condition like a stroke. Seek emergency help."
    elif "internal bleeding" in user_input:
        return "Internal bleeding can be life-threatening. Seek emergency medical help immediately if you suspect internal bleeding."
    elif "loss of sensation" in user_input:
        return "Loss of sensation, especially in the face, arms, or legs, could be a sign of a stroke. Seek immediate medical attention."
    elif "broken ribs" in user_input:
        return "For suspected broken ribs, avoid deep breaths, and seek emergency medical help for evaluation and treatment."
    elif "electrocution" in user_input:
        return "If someone has been electrocuted, disconnect the power source, check for burns or injuries, and seek immediate medical attention."
    elif "swelling in face" in user_input:
        return "Swelling in the face, especially after an injury or allergic reaction, requires immediate medical attention."
    elif "wheezing" in user_input:
        return "Wheezing can indicate asthma or an allergic reaction. Seek medical help immediately if it’s severe or worsening."
    elif "severe cough" in user_input:
        return "A severe cough, especially if accompanied by difficulty breathing or blood, could indicate a serious illness. Seek immediate medical help."
    elif "paralysis" in user_input:
        return "Paralysis, especially if sudden, can be a sign of a stroke or spinal injury. Seek emergency medical help immediately."
    elif "torn ligament" in user_input:
        return "If you suspect a torn ligament, immobilize the area, apply ice, and seek medical attention."
    elif "severe pain after surgery" in user_input:
        return "If you experience severe pain after surgery, contact your doctor or go to the emergency room to rule out complications."
    elif "intense coughing" in user_input:
        return "Intense coughing, especially if it’s productive or prolonged, could indicate a respiratory infection. Seek medical help."
    elif "rash with fever" in user_input:
        return "A rash with a fever can be a sign of a viral or bacterial infection. Seek medical attention to determine the cause."
    elif "depressed breathing" in user_input:
        return "Depressed breathing (shallow or slow) can indicate a serious condition. Seek immediate medical attention."
    elif "headaches with nausea" in user_input:
        return "Headaches accompanied by nausea could indicate a migraine, but if severe, they may suggest a serious issue like a stroke. Seek medical help."
    elif "swollen throat" in user_input:
        return "A swollen throat, especially if it’s causing difficulty breathing, could indicate an allergy or infection. Seek emergency medical attention."
    elif "painful urination" in user_input:
        return "Painful urination can indicate a urinary tract infection or kidney stones. Seek medical help immediately."
    elif "fainting" in user_input:
        return "Fainting can be caused by low blood sugar, dehydration, or a medical condition. Seek immediate medical attention if fainting occurs."
    elif "unusual bruising" in user_input:
        return "Unusual bruising without trauma can be a sign of a bleeding disorder. Consult a healthcare professional immediately."
    elif "rapid heart rate" in user_input:
        return "A rapid heart rate can be caused by stress, fever, or a medical condition. Seek immediate medical attention if accompanied by chest pain or shortness of breath."
    elif "severe nosebleed" in user_input:
        return "Severe nosebleeds that last for more than 20 minutes should be evaluated by a doctor."
    elif "exit" in user_input:
        exit
    else:
        print("sorry out of response will come with a solution in short time sorry for the inconvinent! :)")


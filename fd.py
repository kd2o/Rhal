from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics

# تسجيل خط عربي يدعم العربية
pdfmetrics.registerFont(UnicodeCIDFont('MSung-Light'))  # يدعم العربية بشكل جيد في العرض

# إعداد ملف PDF جديد يدعم العربية
file_path = "English_Grade9_Units1_2_FullSummary_ArabicFixed.pdf"
doc = SimpleDocTemplate(file_path, pagesize=A4)

styles = getSampleStyleSheet()
title = ParagraphStyle('title', fontName='MSung-Light', fontSize=16, alignment=1, leading=20, spaceAfter=12)
subtitle = ParagraphStyle('subtitle', fontName='MSung-Light', fontSize=13, leading=16, spaceAfter=8)
text = ParagraphStyle('text', fontName='MSung-Light', fontSize=11, leading=15)
table_text = ParagraphStyle('table_text', fontName='MSung-Light', fontSize=10, leading=14)

content = []

# العنوان
content.append(Paragraph("📘 English for Palestine – Grade 9 – Term 1", title))
content.append(Paragraph("📖 Full Summary of Units 1 & 2 (Friends and Fun / Healthy Life)", subtitle))
content.append(Spacer(1, 12))

# ---------------------------- UNIT 1 ----------------------------
content.append(Paragraph("الوحدة الأولى: Friends and Fun", subtitle))
content.append(Paragraph("📍 الفكرة الرئيسية: تتحدث الوحدة عن الصداقة، الحياة اليومية، والأنشطة الممتعة التي يقوم بها الطلاب مع أصدقائهم.", text))
content.append(Spacer(1, 10))

# Vocabulary
content.append(Paragraph("🧠 الكلمات الجديدة:", text))
vocab1 = [
    ["الكلمة", "المعنى"],
    ["friendly", "ودود"],
    ["hobby", "هواية"],
    ["together", "معًا"],
    ["sometimes", "أحيانًا"],
    ["always", "دائمًا"],
    ["usually", "عادةً"],
    ["play", "يلعب"],
    ["watch", "يشاهد"],
    ["ride", "يركب"],
    ["visit", "يزور"],
    ["go out", "يخرج"],
    ["meet", "يقابل"],
    ["fun", "مرح / تسلية"]
]
table_vocab1 = Table(vocab1, colWidths=[150, 250])
table_vocab1.setStyle(TableStyle([("GRID", (0,0), (-1,-1), 0.5, colors.black)]))
content.append(table_vocab1)
content.append(Spacer(1, 10))

# Grammar Unit 1
content.append(Paragraph("✏️ القواعد:", subtitle))
content.append(Paragraph("1️⃣ المضارع البسيط (Present Simple Tense):", text))
content.append(Paragraph("نستخدمه للحديث عن العادات، والحقائق، والأفعال المتكررة.", text))
data1 = [
    ["الفاعل", "الفعل", "مثال"],
    ["I / You / We / They", "play / eat / go", "I play football every day."],
    ["He / She / It", "plays / eats / goes", "She eats breakfast at 7."]
]
table1 = Table(data1, colWidths=[120, 150, 200])
table1.setStyle(TableStyle([("GRID", (0,0), (-1,-1), 0.5, colors.black)]))
content.append(table1)
content.append(Spacer(1, 8))
content.append(Paragraph("❌ النفي: don't / doesn't + الفعل<br/>✅ السؤال: Do / Does + الفاعل + الفعل؟", table_text))
content.append(Spacer(1, 10))

# Adverbs of Frequency
content.append(Paragraph("2️⃣ ظروف التكرار (Adverbs of Frequency):", text))
data2 = [
    ["الكلمة", "المعنى", "مثال"],
    ["always", "دائمًا", "I always brush my teeth."],
    ["usually", "عادةً", "She usually walks to school."],
    ["often", "غالبًا", "We often play football."],
    ["sometimes", "أحيانًا", "He sometimes watches TV."],
    ["rarely", "نادراً", "They rarely eat fast food."],
    ["never", "أبدًا", "I never smoke."]
]
table2 = Table(data2, colWidths=[100, 150, 270])
table2.setStyle(TableStyle([("GRID", (0,0), (-1,-1), 0.5, colors.black)]))
content.append(table2)

content.append(PageBreak())

# ---------------------------- UNIT 2 ----------------------------
content.append(Paragraph("الوحدة الثانية: Healthy Life", subtitle))
content.append(Paragraph("📍 الفكرة الرئيسية: تتحدث الوحدة عن الأطعمة الصحية والعادات الجيدة للحفاظ على اللياقة والصحة.", text))
content.append(Spacer(1, 10))

# Vocabulary Unit 2
content.append(Paragraph("🧠 الكلمات الجديدة:", text))
vocab2 = [
    ["الكلمة", "المعنى"],
    ["healthy", "صحي"],
    ["meal", "وجبة"],
    ["diet", "نظام غذائي"],
    ["exercise", "تمارين"],
    ["sugar", "سكر"],
    ["rice", "رز"],
    ["milk", "حليب"],
    ["bread", "خبز"],
    ["fruit", "فاكهة"],
    ["vegetable", "خضار"],
    ["water", "ماء"],
    ["protein", "بروتين"],
    ["fat", "دهون"]
]
table_vocab2 = Table(vocab2, colWidths=[150, 250])
table_vocab2.setStyle(TableStyle([("GRID", (0,0), (-1,-1), 0.5, colors.black)]))
content.append(table_vocab2)
content.append(Spacer(1, 10))

# Grammar Unit 2
content.append(Paragraph("✏️ القواعد:", subtitle))
content.append(Paragraph("1️⃣ الأسماء المعدودة وغير المعدودة (Countable and Uncountable Nouns):", text))
data3 = [
    ["النوع", "أمثلة", "يُستخدم معه"],
    ["معدودة (Countable)", "apple, book, car", "a / an / many / few"],
    ["غير معدودة (Uncountable)", "water, rice, milk, sugar", "much / a lot of / little"]
]
table3 = Table(data3, colWidths=[150, 180, 170])
table3.setStyle(TableStyle([("GRID", (0,0), (-1,-1), 0.5, colors.black)]))
content.append(table3)
content.append(Spacer(1, 8))

content.append(Paragraph("2️⃣ How much / How many:", text))
data4 = [
    ["السؤال", "يُستخدم مع", "مثال"],
    ["How much", "الأسماء غير المعدودة", "How much milk do you drink?"],
    ["How many", "الأسماء المعدودة", "How many apples do you eat?"]
]
table4 = Table(data4, colWidths=[120, 180, 200])
table4.setStyle(TableStyle([("GRID", (0,0), (-1,-1), 0.5, colors.black)]))
content.append(table4)
content.append(Spacer(1, 8))

content.append(Paragraph("3️⃣ محددات الكمية (Quantifiers):", text))
data5 = [
    ["الكلمة", "الاستخدام", "مثال"],
    ["a lot of / lots of", "مع المعدود وغير المعدود", "I have a lot of friends."],
    ["some", "في الجمل المثبتة", "I have some juice."],
    ["any", "في النفي أو السؤال", "I don’t have any sugar."],
    ["few / a few", "مع المعدود", "I have a few books."],
    ["little / a little", "مع غير المعدود", "There is a little milk."]
]
table5 = Table(data5, colWidths=[120, 160, 220])
table5.setStyle(TableStyle([("GRID", (0,0), (-1,-1), 0.5, colors.black)]))
content.append(table5)
content.append(Spacer(1, 12))

content.append(Paragraph("✅ تعبيرات مهمة (Useful Expressions):", subtitle))
content.append(Paragraph("• I eat healthy food every day.<br/>• You should drink a lot of water.<br/>• Don’t eat too much sugar.<br/>• How often do you exercise?", table_text))

# حفظ الملف
doc.build(content)

file_path
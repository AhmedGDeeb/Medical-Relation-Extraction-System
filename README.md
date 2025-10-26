# Medical Relation Extraction System - نظام استخراج العلاقات الطبية

<div dir="rtl">

# نظام استخراج العلاقات الطبية - Medical Relation Extraction System

</div>

## 📋 Project Overview / نظرة عامة على المشروع

This project implements a rule-based information extraction system for Arabic medical texts, focusing on detecting treatment-disease relationships. The system uses linguistic templates and natural language processing techniques to extract semantic relationships from medical documents.

<div dir="rtl">

هذا المشروع يطبق نظام استخراج معلومات قواعدياً للنصوص الطبية العربية، مع التركيز على اكتشاف العلاقات بين الأدوية والأمراض. يستخدم النظام قوالب لغوية وتقنيات معالجة اللغة الطبيعية لاستخراج العلاقات الدلالية من الوثائق الطبية.
</div>

## 🎯 Project Objectives / أهداف المشروع

- Build a simplified information extraction system for medical domain
- Detect treatment-disease relationships from Arabic medical texts
- Implement rule-based approach using linguistic templates
- Extract relationships in the format: `treatment(X, Y)`
- Evaluate system performance and analyze error patterns

<div dir="rtl">

- بناء نظام مبسط لاستخراج المعلومات في المجال الطبي
- اكتشاف العلاقات بين العلاجات والأمراض من النصوص الطبية العربية
- تطبيق منهجية قواعدية باستخدام قوالب لغوية
- استخراج العلاقات بصيغة: `علاج(X, Y)`
- تقييم أداء النظام وتحليل أنماط الأخطاء
</div>

## 🛠️ Installation & Setup / التثبيت والإعداد

### Prerequisites / المتطلبات الأساسية

- Python 3.8 or higher
- Arabic text processing libraries
- Medical corpus of approximately 10,000 words

<div dir="rtl">

- Python 3.8 أو أعلى
- مكتبات معالجة النصوص العربية
- مدونة نصوص طبية بحوالي 10,000 كلمة
</div>

### Install Dependencies / تثبيت المكتبات المطلوبة

```bash
# Install required Python packages
pip install -r requirements.txt
```

Or install individually:

```bash
pip install nltk spacy camel-tools pyarabic tashaphyne
pip install pandas numpy scikit-learn matplotlib
pip install requests beautifulsoup4 regex
```

### Required Libraries / المكتبات المطلوبة

- **nltk**: Natural language processing toolkit
- **spacy**: Advanced NLP with Arabic support
- **camel-tools**: Arabic NLP tools and models
- **pyarabic**: Arabic text processing utilities
- **pandas**: Data manipulation and analysis
- **scikit-learn**: Machine learning and evaluation metrics

<div dir="rtl">

- **nltk**: أدوات معالجة اللغة الطبيعية
- **spacy**: معالجة متقدمة للغة مع دعم العربية
- **camel-tools**: أدوات ونماذج معالجة اللغة العربية
- **pyarabic**: أدوات معالجة النصوص العربية
- **pandas**: معالجة وتحليل البيانات
- **scikit-learn**: التعلم الآلي ومقاييس التقييم
</div>

## 🏗️ System Architecture / هيكلية النظام

### Core Components / المكونات الأساسية

```
medical_relation_extraction/
│
├── 📁 data/
│   ├── 📁 raw/
│   │   └── medical_corpus.txt
│   ├── 📁 processed/
│   │   └── processed_corpus.json
│   └── 📁 evaluation/
│       └── gold_standard.json
│
├── 📁 src/
│   ├── 📄 data_collection.py
│   ├── 📄 template_manager.py
│   ├── 📄 text_processor.py
│   ├── 📄 relation_extractor.py
│   ├── 📄 evaluator.py
│   └── 📄 utils.py
│
├── 📁 templates/
│   ├── 📄 treatment_templates.json
│   └── 📄 expanded_templates.json
│
├── 📁 results/
│   ├── 📄 extracted_relations.json
│   ├── 📄 evaluation_report.txt
│   └── 📄 error_analysis.txt
│
├── 📁 config/
│   └── 📄 settings.py
│
├── 📄 main.py
├── 📄 requirements.txt
├── 📄 project_report.pdf
└── 📄 README.md
```

## 🔄 Implementation Phases / مراحل التنفيذ

### Phase 1: Template Design / المرحلة 1: تصميم القوالب

**Core Templates / القوالب الأساسية:**
- "يستخدم X في علاج Y"
- "يعالج X مرض Y"
- "شفي المصابون بـ Y بعد إعطائهم X"

**Innovated Templates / القوالب المبتكرة:**
- "يساعد X في التخفيف من Y"
- "يوصف X لمرضى Y"
- "X فعال ضد Y"
- "يشفي X من Y"

### Phase 2: Template Expansion / المرحلة 2: توسيع القوالب
- Synonym finding using ArabicWordNet and dictionaries
- Automated template variation generation
- Morphological expansion of template patterns

<div dir="rtl">

- إيجاد المرادفات باستخدام ArabicWordNet والقواميس
- توليد أشكال متنوعة للقوالب آلياً
- التوسيع الصرفي لأنماط القوالب
</div>

### Phase 3: Corpus Building / المرحلة 3: بناء المدونة

- Collection of ~10,000 words medical texts
- Diverse medical topics and treatment mentions
- Coverage of various diseases and medications

<div dir="rtl">

- جمع نصوص طبية بحوالي 10,000 كلمة
- مواضيع طبية متنوعة وذكر العلاجات
- تغطية لأمراض وأدوية مختلفة
</div>

### Phase 4: Relation Extraction / المرحلة 4: استخراج العلاقات

- Text preprocessing and sentence segmentation
- Noun phrase and named entity recognition
- Template matching and pattern recognition
- Relation extraction and validation

<div dir="rtl">

- معالجة النصوص وتقسيمها إلى جمل
- التعرف على العبارات الاسمية والكيانات المسماة
- مطابقة القوالب والتعرف على الأنماط
- استخراج العلاقات والتحقق منها
</div>

### Phase 5: Evaluation / المرحلة 5: التقييم
- Precision calculation: `Precision = Correct Relations / Total Extracted Relations`
- Performance metrics and analysis
- Comparison with gold standard

<div dir="rtl">

- حساب الدقة: `الدقة = العلاقات الصحيحة / إجمالي العلاقات المستخرجة`
- مقاييس الأداء والتحليل
- المقارنة مع المعيار الذهبي
</div>

### Phase 6: Error Analysis / المرحلة 6: تحليل الأخطاء

- Classification of error types
- Root cause analysis
- Improvement recommendations

<div dir="rtl">

- تصنيف أنواع الأخطاء
- تحليل الأسباب الجذرية
- توصيات التحسين
</div>

## ⚡ Quick Start / البدء السريع

```python
# Run the main system
python main.py
```

## 📊 Evaluation Metrics / مقاييس التقييم

### Performance Measures / مقاييس الأداء

- **Precision**: Ratio of correct extracted relations
- **Recall**: Ratio of correctly identified true relations  
- **F1-score**: Harmonic mean of precision and recall
- **Error Analysis**: Categorization of mistake types

<div dir="rtl">

- **الدقة**: نسبة العلاقات الصحيحة المستخرجة
- **الاستدعاء**: نسبة العلاقات الحقيقية التي تم التعرف عليها
- **نتيجة F1**: المتوسط التوافقي للدقة والاستدعاء
- **تحليل الأخطاء**: تصنيف أنواع الأخطاء
</div>

## 📄 Project Deliverables / متطلبات تسليم المشروع

### 1. Source Code & Corpus / الكود المصدري والمدونة
- Complete system implementation
- Medical corpus (~10,000 words)
- Documentation and usage instructions

### 2. Technical Report / التقرير التقني
- Solution for phase 1 (template design)
- Explanation of implementation phases
- Testing methodology and evaluation results
- Component descriptions and system architecture

### 3. Demonstration Session / جلسة العرض التوضيحي
- System implementation walkthrough
- Performance evaluation demonstration
- Results analysis and discussion
- Live system operation

<div dir="rtl">

### 1. الكود المصدري والمدونة (2 علامة)
- تنفيذ النظام الكامل
- المدونة الطبية (~10,000 كلمة)
- التوثيق وتعليمات الاستخدام

### 2. التقرير التقني (4 علامات)
- حل المرحلة الأولى (تصميم القوالب)
- شرح مراحل التنفيذ
- منهجية الاختبار ونتائج التقييم
- وصف المكونات وهيكلية النظام

### 3. جلسة العرض التوضيحي (8 علامات)
- شرح تنفيذ النظام
- عرض تقييم الأداء
- تحليل النتائج والمناقشة
- تشغيل النظام مباشرة
</div>

## ⚠️ Troubleshooting / استكشاف الأخطاء

### Common Issues / المشاكل الشائعة

1. **Arabic text encoding problems**:
   ```python
   # Always specify encoding for Arabic text
   with open('file.txt', 'r', encoding='utf-8') as f:
       text = f.read()
   ```

2. **Template matching failures**:
   - Check template patterns and variations
   - Verify text preprocessing steps

3. **Dependency installation issues**:
   ```bash
   pip install --upgrade pip
   python -m spacy download ar_core_web_sm
   ```

<div dir="rtl">

1. **مشاكل ترميز النص العربي**:

</div>

   ```python
   with open('file.txt', 'r', encoding='utf-8') as f:
       text = f.read()
   ```

<div dir="rtl">

2. **فشل في مطابقة القوالب**:
   - تحقق من أنماط القوالب وأشكالها المختلفة
   - تأكد من خطوات معالجة النص

</div>

3. **مشاكل في تثبيت المكتبات**:

<div dir="rtl">

لتثبيت المكاتب:

</div>

   ```bash
   pip install --upgrade pip
   python -m spacy download ar_core_web_sm
   ```


## 🤝 Contributing / المساهمة

To contribute to project development:
1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Add tests and documentation
5. Submit a pull request

<div dir="rtl">

للمساهمة في تطوير المشروع:
1. انسخ المستودع (Fork)
2. أنشئ فرعاً للميزة الجديدة
3. نفّذ التغييرات
4. أضف الاختبارات والتوثيق
5. أرسل طلب الدمج (Pull Request)
</div>

## 📄 License / الترخيص

This project is developed for academic purposes at the Syrian Virtual University as part of the Natural Language Processing course requirements.

<div dir="rtl">

تم تطوير هذا المشروع لأغراض أكاديمية في الجامعة الافتراضية السورية كجزء من متطلبات مادة معالجة اللغات الطبيعية.
</div>

## 👥 Authors / المؤلفون

- **Student**: ahmad deeb
- **Student ID**: 152818
- **Experinece**: senior python developer (+10 years)
- **University**: Syrian Virtual University
- **Program**: Information Engineering
- **Course**: Natural Language Processing - ANL F24
- **Professor**: Dr. Nada Ghneim

<div dir="rtl">

- **الطالب**: أحمد ديب
- **رقم الطالب**: 152818
- **الجامعة**: الجامعة الافتراضية السورية
- **البرنامج**: الهندسة المعلوماتية
- **المقرر**: معالجة اللغات الطبيعية - ANL F24
- **الأستاذ**: د. ندى غنيم
</div>

## 📞 Contact / معلومات التواصل

For questions or technical support:
- Email: ahmad_152818@svuonline.org
- Submission Date: 10/30/2025

<div dir="rtl">

للأسئلة أو الدعم الفني:
- البريد الإلكتروني: ahmad_152818@svuonline.org
- تاريخ التسليم: 10/30/2025
</div>

---

<div dir="rtl">

**© 2025 - الجامعة الافتراضية السورية - برنامج الهندسة المعلوماتية**
</div>

**© 2025 - Syrian Virtual University - Information Engineering Program**

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
num_samples = 1000  # عدد العينات (المستخدمين)
np.random.seed(42)  # تثبيت العشوائية لضمان نفس النتائج عند كل تشغيل

data = {
    "User_ID": np.random.randint(1000, 5000, num_samples),  # أرقام عشوائية لمعرفات المستخدمين
    "Date": pd.date_range(start="2024-01-01", periods=num_samples, freq="H"),  # أوقات الاستخدام متتالية
    "Data_Usage_MB": np.random.randint(50, 5000, num_samples),  # استهلاك البيانات بين 50 و 5000 ميجابايت
    "Network_Type": np.random.choice(["4G", "5G"], num_samples, p=[0.7, 0.3])  # اختيار عشوائي لنوع الشبكة بنسبة 70% لـ 4G و 30% لـ 5G
}

df = pd.DataFrame(data)  # تحويل القاموس إلى DataFrame (جدول بيانات)
print(df.head())  # عرض أول 5 صفوف من البيانات
print("\n📊 إحصائيات استهلاك البيانات:")
print(df["Data_Usage_MB"].describe())  # تحليل إحصائي لاستهلاك البيانات
high_usage_threshold = df["Data_Usage_MB"].quantile(0.90)  # أعلى 10% من المستخدمين
low_usage_threshold = df["Data_Usage_MB"].quantile(0.10)  # أقل 10% من المستخدمين

df["Usage_Category"] = df["Data_Usage_MB"].apply(
    lambda x: "عالي" if x > high_usage_threshold else ("منخفض" if x < low_usage_threshold else "متوسط")
)
plt.figure(figsize=(8, 5))
sns.histplot(df["Data_Usage_MB"], bins=30, kde=True, color="blue")
plt.title("توزيع استهلاك البيانات")
plt.xlabel("استهلاك البيانات (MB)")
plt.ylabel("عدد المستخدمين")
plt.show()

df["Hour"] = df["Date"].dt.hour  # استخراج الساعة من التاريخ
usage_per_hour = df.groupby("Hour")["Data_Usage_MB"].mean()  # حساب متوسط الاستهلاك لكل ساعة
plt.figure(figsize=(8, 5))
sns.lineplot(x=usage_per_hour.index, y=usage_per_hour.values, marker="o", color="red")
plt.title("متوسط استهلاك البيانات خلال ساعات اليوم")
plt.xlabel("الساعة")
plt.ylabel("متوسط الاستهلاك (MB)")
plt.xticks(range(0, 24))  # التأكد من عرض كل الساعات من 0 إلى 23
plt.grid()
plt.show()
plt.figure(figsize=(6, 4))
sns.stripplot(x=df["Network_Type"], y=df["Data_Usage_MB"], jitter=True, palette=["orange", "green"])
plt.title("مقارنة استهلاك البيانات بين شبكتي 4G و 5G (مخطط النقاط)")
plt.xlabel("نوع الشبكة")
plt.ylabel("استهلاك البيانات (MB)")
plt.show()



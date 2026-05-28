# 🔐 Password Strength Checker

একটি সহজ Python প্রোগ্রাম যা আপনার পাসওয়ার্ডের শক্তি পরীক্ষা করে।

---

## 📋 বৈশিষ্ট্য

এই প্রোগ্রামটি পাসওয়ার্ড চেক করে এবং বলে:
- ✅ **Strong Password** (শক্তিশালী)
- ⚠️ **Medium Password** (মাঝারি)
- ❌ **Weak Password** (দুর্বল)

---

## 🔍 কীভাবে কাজ করে?

প্রোগ্রামটি নিম্নলিখিত ৫টি বিষয় চেক করে:

| চেক | শর্ত | উদাহরণ |
|------|------|--------|
| 📏 দৈর্ঘ্য | কমপক্ষে ৮ ক্যারেক্টার | `MyPass@123` (১০ চিহ্ন) |
| 🔤 বড় হাতের অক্ষর | A-Z | `MyPass@123` (M, P) |
| 🔡 ছোট হাতের অক্ষর | a-z | `MyPass@123` (y, a, s, s) |
| 🔢 সংখ্যা | 0-9 | `MyPass@123` (1, 2, 3) |
| ⚡ বিশেষ চিহ্ন | @$!%*?& | `MyPass@123` (@) |

---

## 📊 পাসওয়ার্ড শক্তির স্তর

| শক্তি | শর্ত পূরণ | উদাহরণ |
|------|----------|--------|
| 🔴 **Weak** | ≤ ২টি শর্ত | `abc`, `password` |
| 🟡 **Medium** | ৩-৪টি শর্ত | `Abc123`, `Pass123` |
| 🟢 **Strong** | সব ৫টি শর্ত | `MyPass@123`, `Secure#999` |

---

## 🚀 চালানোর নিয়ম

### **পদ্ধতি ১: Command Prompt/Terminal (সবচেয়ে সহজ)**

**Windows:**
```bash
python main.py
```

**Mac/Linux:**
```bash
python3 main.py
```

### **পদ্ধতি ২: Online Python Compiler**

এই সাইটে যান এবং কোড পেস্ট করুন:
- [Replit.com](https://replit.com)
- [OnlineGDB.com](https://www.onlinegdb.com)
- [Ideone.com](https://ideone.com)

---

## 💻 উদাহরণ

```
=== Password Strength Checker ===
Enter your password: MyPass@123
Strong Password
```

```
=== Password Strength Checker ===
Enter your password: abc
Weak Password
```

```
=== Password Strength Checker ===
Enter your password: Abc123
Medium Password
```

---

## ✅ সেরা পাসওয়ার্ডের টিপস

✨ একটি শক্তিশালী পাসওয়ার্ড তৈরির জন্য:
- ন্যূনতম ৮ অক্ষর ব্যবহার করুন
- বড় এবং ছোট হাতের অক্ষর মিশান
- অন্তত একটি সংখ্যা যোগ করুন
- বিশেষ চিহ্ন (@, $, !, %, *, ?, &) ব্যবহার করুন
- সাধারণ শব্দ এড়িয়ে চলুন

---

## 👨‍💻 ডেভেলপার

**Apan2026**

---

## 📄 লাইসেন্স

এই প্রজেক্ট Open Source এবং সবার জন্য উপলব্ধ।

---

**আপনার পাসওয়ার্ড নিরাপদ রাখুন! 🔐**

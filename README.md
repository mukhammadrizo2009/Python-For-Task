# Python-For-Task

# 🔄 Python: `for` tsikli bo'yicha amaliy mashqlar

Ushbu vazifalar `for` tsikli, `range()` funksiyasi va elementlarni aylanib chiqish (iteration) bo'yicha bilimlaringni mustahkamlaydi.

## 🟢 Oddiy daraja (Asoslar)

### 1. Sonlarni chiqarish
`range()` dan foydalanib 1 dan 10 gacha bo'lgan sonlarni konsolga chiqaring.
* **Natija:** 1, 2, 3... 10

### 2. Ismlarni salomlash
Ismlar ro'yxati berilgan: `ismlar = ["Ali", "Vali", "Gani"]`. Har bir ismga "Salom, [ism]" deb xabar chiqaring.

### 3. Kvadratlar jadvali
1 dan 5 gacha bo'lgan sonlarning kvadratini chiqaring.
* **Misol:** "2 ning kvadrati 4 ga teng"

### 4. Faqat juft sonlar
1 dan 20 gacha bo'lgan faqat juft sonlarni konsolga chiqaring.
* **Yordam:** `range(start, stop, step)` dan foydalaning.

### 5. Teskari sanoq
10 dan 1 gacha teskari tartibda sonlarni chiqaring.

---

## 🟡 O'rta daraja (Mantiqiy amallar)

### 6. Yig'indini hisoblash
1 dan 100 gacha bo'lgan barcha sonlarning yig'indisini `for` yordamida hisoblang.
* **Natija:** 5050

### 7. Ro'yxat elementlari yig'indisi
Sonlar ro'yxati berilgan: `sonlar = [10, 20, 30, 40]`. Ularning yig'indisini `sum()` funksiyasisiz, faqat `for` orqali toping.

### 8. So'zdagi harflar
Foydalanuvchi kiritgan so'zning har bir harfini alohida qatorda chiqaring.

### 9. Belgilarni sanash
Berilgan string ichida nechta "a" harfi borligini `for` tsikli yordamida sanang.
* **Misol:** "banana" -> 3 ta

### 10. Faqat musbat sonlar
Aralash sonlar ro'yxatidan faqat musbatlarini ajratib yangi listga joylang.
* **Input:** `[1, -5, 2, -8, 10]` -> **Output:** `[1, 2, 10]`

### 11. Karra jadvali
Foydalanuvchi kiritgan sonning (masalan 5) 1 dan 10 gacha bo'lgan karra jadvalini chiqaring.
* **Misol:** `5 x 1 = 5`, `5 x 2 = 10`...

### 12. List ichida qidiruv
Mevalar ro'yxatidan "Olma" bor yoki yo'qligini `for` orqali tekshiring. Agar bo'lsa "Topildi" deb chiqaring.

---

## 🔴 Qiyinroq daraja (Algoritmlar)

### 13. Eng katta sonni topish
`max()` funksiyasisiz, `for` yordamida list ichidagi eng katta sonni toping.

### 14. Faktorial hisoblash
Berilgan sonning faktorialini hisoblang ($n!$).
* **Misol:** $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$

### 15. Elementlar turi
Har xil turdagi elementlardan iborat list berilgan. Har bir elementning turini (type) chiqaring.
* **Input:** `[5, "salom", 3.14, True]`

### 16. To'xtatish (break)
1 dan 100 gacha sonlarni aylaning, lekin son 25 ga yetganda tsiklni to'xtating.

### 17. O'tkazib yuborish (continue)
1 dan 10 gacha sonlarni chiqaring, faqat 5 va 7 sonlarini tashlab o'tib keting.

### 18. Ichma-ich tsikl (Nested loop)
Quyidagi shaklni chiqaring:

### 19. Ro'yxatni filtrlash
Berilgan ismlar ro'yxatidan faqat "A" harfi bilan boshlanadiganlarini alohida listga ajrating.

### 20. O'rtacha qiymat
Talabalarning baholari listi berilgan. `for` yordamida ularning o'rtacha bahosini hisoblang.
* **Yordam:** (Yig'indi / soni)
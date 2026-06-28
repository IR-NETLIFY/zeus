<div align="center">
  <img width="100%" alt="Zeus Panel Interface" src="https://raw.githubusercontent.com/IR-NETLIFY/zeus/refs/heads/main/photos/deployer.png" style="border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.2);" />
  <img width="100%" alt="Zeus Panel Status" src="https://raw.githubusercontent.com/IR-NETLIFY/zeus/refs/heads/main/photos/updater.png" style="border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.2);" />
  <img width="100%" alt="Zeus Panel Interface" src="https://raw.githubusercontent.com/IR-NETLIFY/zeus/refs/heads/main/photos/dark.png" style="border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.2);" />
  <br><br>
  <img width="100%" alt="Zeus Panel Status" src="https://raw.githubusercontent.com/IR-NETLIFY/zeus/refs/heads/main/photos/light.png" style="border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.2);" />
  
  <br><br>

  <h1>⚡️ پنل زئوس (Zeus Panel)</h1>
  <strong>سیستم پیشرفته مدیریت کانفیگ VLESS روی Cloudflare Workers + D1</strong>

  <br><br>

  <p>
    <a href="https://github.com/IR-NETLIFY/zeus"><img src="https://img.shields.io/badge/Version-1.2.12-0052CC?style=for-the-badge&logo=semver&logoColor=white" alt="Version"></a>
    <a href="https://cloudflare.com"><img src="https://img.shields.io/badge/Platform-Cloudflare_Workers-F38020?style=for-the-badge&logo=cloudflare&logoColor=white" alt="Platform"></a>
    <a href="https://t.me/IR_NETLIFY"><img src="https://img.shields.io/badge/Developer-IR__NETLIFY-00792D?style=for-the-badge&logo=telegram&logoColor=white" alt="Developer"></a>
  </p>
</div>

---

> [!NOTE]
> **معرفی کوتاه:** پنل زئوس یک پلتفرم کامل با رابط کاربری اختصاصی است که نیازی به سرور ندارد. این پنل به صورت ۱۰۰٪ روی زیرساخت رایگان کلودفلر اجرا شده و به شما امکان ساخت، مدیریت و ارائه اشتراک به کاربران را با بالاترین سطح تنظیمات (Fragment و IP تمیز) می‌دهد.

## ✨ قابلیت‌های سیستم

* 👥 **سیستم اکانتینگ پیشرفته (D1):** تعریف دقیق حجم مجاز (GB) و روزهای اعتبار برای هر کاربر به صورت مجزا با قطع خودکار هنگام اتمام اشتراک.
* 🛡 **بایپس فیلترینگ قدرتمند:** پشتیبانی کامل از تنظیمات `Fragment` (تنظیم Length و Interval) و شبیه‌سازی اثر انگشت مرورگرها (Fingerprint) نظیر iOS، Chrome و Randomized.
* 📡 **انتخاب‌گر هوشمند آی‌پی (Clean IP):** دریافت خودکار لیست آپدیت شده آی‌پی‌های تمیز کلودفلر برای اپراتورهای مختلف (MCI, Irancell, Shatel و...) مستقیماً از گیت‌هاب و اعمال روی کاربران.
* 📊 **مانیتورینگ زنده API کلودفلر:** ادغام با `Cloudflare GraphQL` برای نمایش لحظه‌ای درخواست‌های (Requests) مصرف‌شده‌ی امروز و ۳۰ روز گذشته اکانت کلودفلر شما جهت جلوگیری از مسدودی.
* 🔄 **آپدیت درون‌برنامه‌ای (OTA):** دریافت نسخه‌های جدید پنل تنها با فشردن دکمه «بررسی آپدیت» در منوی تنظیمات، بدون کوچکترین اختلال در دیتابیس کاربران.
* 🔗 **اشتراک‌های چندگانه:** ارائه لینک‌های ساب‌اسکریپشن هوشمند (متنی ساده + فرمت مدرن JSON) همراه با پشتیبانی همزمان از پورت‌های امن (TLS) و عادی (Non-TLS).

---

## 🚀 راهنمای نصب تمام خودکار (Zero-Touch)

> [!IMPORTANT]  
> **نصب آسان:** سیستم دیپلوی اختصاصی زئوس تمام مراحل از جمله ساخت دیتابیس، ساخت ورکر، اتصال متغیرها و فعال‌سازی لینک‌ها را در کسری از ثانیه **بدون نیاز به نوشتن حتی یک خط کد** برای شما انجام می‌دهد.

۱. **ورود به سایت دیپلوی:** ابتدا به سایت استقرار خودکار مراجعه نمایید:

<br>
<div align="center">
  <h2>🚀 <a href="https://zeus-panel.ir-netlify.workers.dev/"><b>ورود به سایت پنل زئوس</b></a> 🚀</h2>
  <a href="https://zeus-panel.ir-netlify.workers.dev/"><img src="https://img.shields.io/badge/Deploy-Zeus_Panel-00792D?style=for-the-badge&logo=cloudflare&logoColor=white" alt="Deploy Zeus"></a>
  <br><br>
  <a href="https://zeus-panel.ir-netlify.workers.dev/" dir="ltr"><b>https://zeus-panel.ir-netlify.workers.dev</b></a>
</div>
<br>

۲. **اخذ مجوز (Token):** بر روی گزینه **«دریافت توکن»** کلیک نمایید. این لینک شما را به پنل کلودفلر هدایت نموده تا دسترسی‌های امنیتی لازم (Permissions) جهت استقرار منابع ایجاد گردد. در انتهای صفحه باز شده، توکن را تایید و کپی کنید.

۳. **آغاز فرآیند:** توکن دریافت شده را در فیلد مربوطه در پورتال استقرار وارد نموده و گزینه **«ساخت پنل»** را انتخاب کنید.

۴. **اتمام و ورود:** پس از گذشت چند ثانیه و اتمام عملیات، لینک دسترسی به پنل مدیریت در اختیار شما قرار خواهد گرفت. (رمز عبور مدیریت در اولین ورود پیکربندی خواهد شد).

> [!WARNING]
> در اولین ورود به آدرس پنلتان (مسیر `/panel` در انتهای آدرس ورکر)، از شما خواسته می‌شود تا یک رمز عبور قدرتمند برای مدیریت سیستم تنظیم کنید. این رمز را فراموش نکنید!

---

## 🛠 امکانات صفحه وضعیت (Status Page)

کاربران شما دارای یک صفحه وضعیت اختصاصی جذاب با طراحی Glassmorphism هستند. آن‌ها با باز کردن لینک وضعیت خود می‌توانند موارد زیر را زنده مشاهده کنند:
- **وضعیت اتصال:** (فعال، مسدود شده دستی، منقضی شده زمانی، تمام شدن حجم).
- **نمودارهای گرافیکی:** مشاهده درصد حجم مصرف‌شده و روزهای باقی‌مانده.
- **تولید بارکد:** نمایش QR Code برای اتصال مستقیم بدون نیاز به کپی کردن لینک.

---
## ⚖️ حق نشر و اعتبارات

این پنل توسط ماکان نوشته شده و من فقط آن را توسعه داده ام:

* ⚙️ **سازنده اصلی پنل زئوس:** [Macan-dev](https://github.com/macan-dev/EasySNI) (پشتیبانی: [@EzAccess1](https://t.me/EzAccess1))
* 🏗 **توسعه‌دهنده سیستم دیپلوی خودکار و ارتقاءدهنده امکانات پنل:** [IR_NETLIFY](https://t.me/IR_NETLIFY)
<br>
<div align="center">
  <blockquote>
    <i>توسعه یافته جهت تضمین ارتباطات پایدار و دسترسی آزاد به اطلاعات. ✌️</i>
  </blockquote>
</div>

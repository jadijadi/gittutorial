# __Jadi's GIT tutorial contents__
# List of git commands
- git config 
    > <p dir="rtl" align="right">برای تنظیمات ابزار به کار می رود. مانند مشخصات نویسنده و همچنین تنظیمات مربوط به پراکسی برای کلاینت گیت</p>

- git config --global user.name "UserName"
    > <p dir="rtl" align="right">برای تنظیمات یوزر نیم استفاده میشود. و در قدم اول بعد از نصب گیت به کار می رود</p>

- git config --global user.email "Email"
    > <p dir="rtl" align="right">برای تنظیمات شناسه ایمیل استفاده میشود. و در قدم اول بعد از نصب گیت به کار می رود</p>

- git config --global user.signingkey sec
    > <p dir="rtl" align="right">برای تنظیمات رمزگذاری استفاده میشود. و در قدم اول بعد از نصب گیت به کار می رود که در آن باید از کلید خصوصی خود استفاده کرد</p>

- git init
    > <p dir="rtl" align="right">شروع کار با git. در عمل یک دایرکتوری به نام دات-گیت می سازد که در سیستم‌عامل‌های یونیکسی در حالت عادی دیده نمی‌شود</p>

- git add fileName
    > <p dir="rtl" align="right">افزودن فایل به git</p>

- git add -A
    > <p dir="rtl" align="right">افزودن همه فایل‌ها به git</p>
    
- git add .
    > <p dir="rtl" align="right">اضافه کردن همه فایل‌های دایرکتوری فعلی به git</p>
    
- git log
    > <p dir="rtl" align="right">commit ها را نمایش میدهد</p>
    
- git log --oneline -N
    > <p dir="rtl" align="right">تعداد N کامیت آخر را به صورت تک خطی نشان می‌دهدد(بجای N، عدد وارد شود)</p>

- git commit -m "Title"
    > <p dir="rtl" align="right">کامیت کردن تغییرات با عنوان</p>

- git commit -m "Title" -m "Description"
    > <p dir="rtl" align="right">کامیت کردن تغییرات با عنوان و توضیحات</p>

- git commit -am 'Title'
    > <p dir="rtl" align="right">کامیت کردن تغییرات فایلی که قبلا گیت آن را شناخته، بدون نیاز به add کردن</p>

- git status
    > <p dir="rtl" align="right">نمایش وضعیت</p>

- git clean
    > <p dir="rtl" align="right">حذف فایل های track نشده توسط گیت</p>
- git reset fileName
    > <p dir="rtl" align="right">خارج کردن فایل از حالت stage</p>

- git diff HEAD
    > <p dir="rtl" align="right">نمایش وضعیت فعلی نسبت به وضعیت آخرین کامیت</p>

- git diff --staged
    > <p dir="rtl" align="right">نمایش وضعیت فعلی نسبت به وضعیت stage</p>

- git diff branchName
    > <p dir="rtl" align="right">نمایش تغییرات مستر نسبت به برنچ وارد شده</p>

- git checkout --fileName
    > <p dir="rtl" align="right">فایل را از آخرین کامیت استخراج کرده و جایگزین فایل فعلی می کند</p>

- git reset fileName
    > <p dir="rtl" align="right">اگر فایل به مرحله رو به مرحله استیج برده باشیم و بخوایم از استیج خارجش کنیم.</p>

- git reset commitHash
    > <p dir="rtl" align="right">بازگشت به کامیت اشاره شده، در حالی که تغییرات unstage شده اند</p>

- git reset --hard commitHash
    > <p dir="rtl" align="right">بازگشت به کامیت اشاره شده، در حالی که تغییرات کامل از بین رفته اند</p>

- git branch 
    > <p dir="rtl" align="right">نمایش شاخه‌های موجود</p>

- git branch branchName
    > <p dir="rtl" align="right">ساخت شاخه جدید با نام تعیین شده</p>

- git checkout -b branchName
    > <p dir="rtl" align="right">ساخت و سوئیچ کردن همزمان به شاخه جدید با نام تعیین شده</p>

- git checkout branchName
    > <p dir="rtl" align="right">سوئیچ کردن از شاخه فعلی به شاخه تعیین شده</p>

- git merge branchName
    > <p dir="rtl" align="right">شاخه مذکور را با شاخه فعلی ادغام می کند</p>

- git rm fileName
    > <p dir="rtl" align="right">حذف فایل از git و از فایل سیستم</p>

- git checkout HEAD fileName
    > <p dir="rtl" align="right">باز گرداندن فایل پس از استفاده کامند rm</p>

- git branch -d branchName
    > <p dir="rtl" align="right">حذف شاخه</p>

- git branch -M branchName
    > <p dir="rtl" align="right">ایجاد شاخه اصلی بجای شاخه مستر</p>

- git push origin master
    > <p dir="rtl" align="right">شاخه master را به origin ارسال می کند</p>

- git pull origin master
    > <p dir="rtl" align="right">شاخه master را از origin دریافت می کند</p>

- git remote 
    > <p dir="rtl" align="right">نمایش remote</p>

- git remote add origin url
    > <p dir="rtl" align="right">افزودن remote با آدرس تعیین شده و نام origin</p>

- git show commitID
    > <p dir="rtl" align="right">نمایش جزئیات commit با شناسه تعیین شده</p>

- git tag
    > <p dir="rtl" align="right">نمایش تگ ها</p>

- git tag -a tagName -m "description"
    > <p dir="rtl" align="right">افزودن تگ با نام و توضیحات تعیین شده</p>

- git show tagName
    > <p dir="rtl" align="right">نمایش جزئیات تگ</p>

- git blame fileName -L lineNumber
    > <p dir="rtl" align="right">مشاهده اینکه از خط مذکور تا انتهای فایل را چه کسی نوشته است</p>
    
- git blame fineName -L lineNumber, lineNumber 
    > <p dir="rtl" align="right">مشاهده اینکه  خط مذکور را چه کسی نوشته است</p>

- git bisect 
    > <p dir="rtl" align="right">برای debug به کار می رود</p>
    
- git bisect reset
    > <p dir="rtl" align="right">و برگشت به سر مغازه از نواستفاده میشود   bisect reset برای متوقف کردن  از دستور </p>

- git Config --global user.name userName
    > <p dir="rtl" align="right">ست کردن یوزرنیم</p>

- git Config --global user.email emailAddress
    > <p dir="rtl" align="right">ست کردن ایمیل</p>

- git stash
    > <p dir="rtl" align="right">اگر وسط کاری هستید و نمیخواهید که کامیت کنید میتونید با این دستور تغیرات جدید رو بفرستید توی stash</p>

- git stash list
    > <p dir="rtl" align="right">نمایش لیست stash ها</p>

- git stash pop stash@{0}
    > <p dir="rtl" align="right">برگرداندن به حالت آخرین stash البته میتونید آیدی ها دیگه ای هم بزنید </p>

- git clone repositoryAddress
    > <p dir="rtl" align="right"> یک کلون از مخزنی که آدرس آن را وارد کردیم در پوشه ای جدید با اسم همان مخزن ایجاد می کند </p>

- git remote remove remoteName
    > <p dir="rtl" align="right"> حذف کردن یک ریموت </p>

- git remote rename oldName newName
    > <p dir="rtl" align="right"> تغییر نام یک ریموت </p>

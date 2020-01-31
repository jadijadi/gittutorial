# __Jadi's GIT tutorial contents__
# List of git commands
- git init
    > <p dir="rtl" align="right">شروع کار با git</p>

- git add fileName
    > <p dir="rtl" align="right">افزودن فایل به git</p>

- git add -A
    > <p dir="rtl" align="right">اضافه کردن همه فایل‌ها به git</p>

- git commit -m "description"
    > <p dir="rtl" align="right">کامیت کردن تغییرات با توضیحات</p>

- git status
    > <p dir="rtl" align="right">نمایش وضعیت</p>

- git reset fileName
    > <p dir="rtl" align="right">خارج کردن فایل از حالت stage</p>

- git diff HEAD
    > <p dir="rtl" align="right">نمایش وضعیت فعلی نسبت به وضعیت آخرین کامیت</p>

- git diff --staged
    > <p dir="rtl" align="right">نمایش وضعیت فعلی نسبت به وضعیت stage</p>

- git checkout --fileName
    > <p dir="rtl" align="right">فایل را از آخرین کامیت استخراج کرده و جایگزین فایل فعلی می کند</p>

- git branch 
    > <p dir="rtl" align="right">نمایش شاخه‌های موجود</p>

- git branch branchName
    > <p dir="rtl" align="right">ساخت شاخه جدید با نام تعیین شده</p>

- git checkout branchName
    > <p dir="rtl" align="right">سوئیچ کردن از شاخه فعلی به شاخه تعیین شده</p>

- git merge branchName
    > <p dir="rtl" align="right">شاخه مذکور را با شاخه فعلی ادغام می کند</p>

- git rm fileName
    > <p dir="rtl" align="right">حذف فایل از git و از فایل سیستم</p>

- git branch -d branchName
    > <p dir="rtl" align="right">حذف شاخه</p>

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

- git tag -a tagName -m "description
    > <p dir="rtl" align="right">افزودن تگ با نام و توضیحات تعیین شده</p>

- git show tagName
    > <p dir="rtl" align="right">نمایش جزئیات تگ</p>

- git blame fileName -L lineNumber
    > <p dir="rtl" align="right">مشاهده اینکه از خط مذکور تا انتهای فایل را چه کسی نوشته است</p>
    
-git blame fineName -L lineNumber, lineNumber 
    > <p dir="rtl" align="right">مشاهده اینکه  خط مذکور را چه کسی نوشته است</p>

- git bisect 
    > <p dir="rtl" align="right">برای debug به کار می رود</p>
    
- git config 
    > <p dir="rtl" align="right">برای تنظیمات ابزار به کار می رود. مانند مشخصات نویسده و همچنین تنظیمات مربوط به پراکسی برای کلاینت گیت</p>


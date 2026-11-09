# Rift Runner ProGuard Rules
# Keep WebView interface
-keepclassmembers class * extends android.webkit.WebViewClient {
    public *;
}
-keepclassmembers class * extends android.webkit.WebChromeClient {
    public *;
}
-keep class com.kirostudios.riftrunner.** { *; }

ALL_MODE = [
    ["title", "App", True, "(str) Title of your application", '\n'],
    ["package.name", "App", True, "(str) Package name", '\n'],
    ["package.domain", "org.app.test", True, "(str) Package domain (needed for android/ios packaging)", '\n'],
    ["source.dir", ".", True, "(str) Source code where the main.py live", '\n'],
    ["source.include_exts", "py,png,jpg,kv,atlas,ttf,mp3,json,wav,ico", True, "(list) Source files to include (let empty to include all the files)", '\n'],
    ["source.include_patterns", "assets/*,images/*.png", False, "(list) List of inclusions using pattern matching", '\n'],
    ["source.exclude_exts", "spec", False, "(list) Source files to exclude (let empty to not exclude anything)", '\n'],
    ["source.exclude_dirs", "tests, bin, venv", False, "(list) List of directory to exclude (let empty to not exclude anything)", '\n'],
    ["source.exclude_patterns", "license,images/*/*.jpg", False, "(list) List of exclusions using pattern matching\nDo not prefix with './'", '\n'],
    ["version", "0.0.1", True, "(str) Application versioning (method 1)", '\n'],
    ["version.regex", "__version__ = ['\"](.*)['\"]", False, "(str) Application versioning (method 2)", ''],
    ["version.filename", "%(source.dir)s/main.py", False, '', '\n'],
    ["requirements", "python3,kivy", True, "(list) Application requirements\ncomma separated e.g. requirements = sqlite3,kivy", '\n'],
    ["requirements.source.kivy", "../../kivy", False, "(str) Custom source folders for requirements\nSets custom source for any requirements with recipes", '\n'],
    ["presplash.filename", "%(source.dir)s/rasset/icon/presplash.png", True, "(str) Presplash of the application", '\n'],
    ["icon.filename", "%(source.dir)s/rasset/icon/mainicon.ico", True, "(str) Icon of the application", '\n'],
    ["orientation", "portrait", True, "(str) Supported orientation (one of landscape, sensorLandscape, portrait or all)", '\n'],
    ["services", "NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY", False, "(list) List of service to declare", '\n\n#\n# OSX Specific\n#\n\n#\n# author = © Copyright Info\n'],
    ["osx.python_version", "3", True, "change the major version of python used by the app", '\n'],
    ["osx.kivy_version", "1.9.1", True, "Kivy version to use", '\n\n#\n# Android specific\n#\n'],
    ["fullscreen", "0", True, "(bool) Indicate if the application should be fullscreen or not", '\n'],
    ["android.presplash_color", "#FFFFFF", False, (
        "(string) Presplash background color (for android toolchain)\n"
        "Supported formats are: #RRGGBB #AARRGGBB or one of the following names:\n"
        "red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,\n"
        "darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,\n"
        "olive, purple, silver, teal."), '\n'],
    ["android.presplash_lottie", "\"path/to/lottie/file.json\"", False, (
        "(string) Presplash animation using Lottie format.\n"
        "see https://lottiefiles.com/ for examples and https://airbnb.design/lottie/\n"
        "for general documentation.\n"
        "Lottie files can be created using various tools, like Adobe After Effect or Synfig."), '\n'],
    ["icon.adaptive_foreground.filename", "%(source.dir)s/data/icon_fg.png", False, "(str) Adaptive icon of the application (used if Android API level is 26+ at runtime)", ''],
    ["icon.adaptive_background.filename", "%(source.dir)s/data/icon_bg.png", False, "", '\n'],
    ["android.permissions", "READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE", True, "(list) Permissions", '\n'],
    ["android.features", "android.hardware.usb.host", False, "(list) features (adds uses-feature -tags to manifest)", '\n'],
    ["android.api", "27", False, "(int) Target Android API, should be as high as possible.", '\n'],
    ["android.minapi", "21", False, "(int) Minimum API your APK / AAB will support.", '\n'],
    ["android.sdk", "20", False, "(int) Android SDK version to use", '\n'],
    ["android.ndk", "23b", False, "(str) Android NDK version to use", '\n'],
    ["android.ndk_api", "21", False, "(int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.", '\n'],
    ["android.private_storage", "True", False, "(bool) Use --private data storage (True) or --dir public storage (False)", '\n'],
    ["android.ndk_path", "", False, "(str) Android NDK directory (if empty, it will be automatically downloaded.)", '\n'],
    ["android.sdk_path", "", False, "(str) Android SDK directory (if empty, it will be automatically downloaded.)", '\n'],
    ["android.ant_path", "", False, "(str) ANT directory (if empty, it will be automatically downloaded.)", '\n'],
    ["android.skip_update", "False", False, (
        "(bool) If True, then skip trying to update the Android sdk\n"
        "This can be useful to avoid excess Internet downloads or save time\n"
        "when an update is due and you just want to test/build your package"), '\n'],
    ["android.accept_sdk_license", "False", False, (
        "(bool) If True, then automatically accept SDK license\n"
        "agreements. This is intended for automation only. If set to False,\n"
        "the default, you will be shown the license when first running\n"
        "buildozer."), '\n'],
    ["android.entrypoint", "org.kivy.android.PythonActivity", False, "(str) Android entry point, default is ok for Kivy-based app", '\n'],
    ["android.activity_class_name", "org.kivy.android.PythonActivity", False, (
        "(str) Full name including package path of the Java class that implements Android Activity\n"
        "use that parameter together with android.entrypoint to set custom Java class instead of PythonActivity"), '\n'],
    ["android.extra_manifest_xml", "./src/android/extra_manifest.xml", False, (
        "(str) Extra xml to write directly inside the <manifest> element of AndroidManifest.xml\n"
        "use that parameter to provide a filename from where to load your custom XML code"), '\n'],
    ["android.extra_manifest_application_arguments", "./src/android/extra_manifest_application_arguments.xml", False, (
        "(str) Extra xml to write directly inside the <manifest><application> tag of AndroidManifest.xml\n"
        "use that parameter to provide a filename from where to load your custom XML arguments:"), '\n'],
    ["android.service_class_name", "org.kivy.android.PythonService", False, (
        "(str) Full name including package path of the Java class that implements Python Service\n"
        "use that parameter to set custom Java class instead of PythonService"), '\n'],
    ["android.apptheme", "\"@android:style/Theme.NoTitleBar\"", False, "(str) Android app theme, default is ok for Kivy-based app", '\n'],
    ["android.whitelist", "", False, "(list) Pattern to whitelist for the whole project", '\n'],
    ["android.whitelist_src", "", False, "(str) Path to a custom whitelist file", '\n'],
    ["android.blacklist_src", "", False, "(str) Path to a custom blacklist file", '\n'],
    ["android.add_jars", "foo.jar,bar.jar,path/to/more/*.jar", False, (
        "(list) List of Java .jar files to add to the libs so that pyjnius can access\n"
        "their classes. Don't add jars that you do not need, since extra jars can slow\n"
        "down the build process. Allows wildcards matching, for example:\n"
        "OUYA-ODK/libs/*.jar"), '\n'],
    ["android.add_src", "", False, (
        "(list) List of Java files to add to the android project (can be java or a\n"
        "directory containing the files)"), '\n'],
    ["android.add_aars", "", False, "(list) Android AAR archives to add", '\n'],
    ["android.add_assets", "", False, (
        "(list) Put these files or directories in the apk assets directory.\n"
        "Either form may be used, and assets need not be in 'source.include_exts'.\n"
        "1) android.add_assets = source_asset_relative_path\n"
        "2) android.add_assets = source_asset_path:destination_asset_relative_path"), '\n'],
    ["android.gradle_dependencies", "", False, "(list) Gradle dependencies to add", '\n'],
    ["android.enable_androidx", "False", False, (
        "(bool) Enable AndroidX support. Enable when 'android.gradle_dependencies'\n"
        "contains an 'androidx' package, or any package from Kotlin source.\n"
        "android.enable_androidx requires android.api >= 28"), '\n'],
    ["android.add_compile_options", "\"sourceCompatibility = 1.8\", \"targetCompatibility = 1.8\"", False, (
        "(list) add java compile options\n"
        "this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option\n"
        "see https://developer.android.com/studio/write/java8-support for further information"), '\n'],
    ["android.add_gradle_repositories", "", False, (
        "(list) Gradle repositories to add {can be necessary for some android.gradle_dependencies}\n"
        "please enclose in double quotes \n"
        "e.g. android.gradle_repositories = \"maven { url 'https://kotlin.bintray.com/ktor' }\""), '\n'],
    ["android.add_packaging_options", "", False, (
        "(list) packaging options to add \n"
        "see https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.PackagingOptions.html\n"
        "can be necessary to solve conflicts in gradle_dependencies\n"
        "please enclose in double quotes \n"
        "e.g. android.add_packaging_options = \"exclude 'META-INF/common.kotlin_module'\", \"exclude 'META-INF/*.kotlin_module'\""), '\n'],
    ["android.add_activities", "com.example.ExampleActivity", False, "(list) Java classes to add as activities to the manifest.", '\n'],
    ["android.ouya.category", "GAME", False, (
        "(str) OUYA Console category. Should be one of GAME or APP\n"
        "If you leave this blank, OUYA support will not be enabled"), '\n'],
    ["android.ouya.icon.filename", "%(source.dir)s/data/ouya_icon.png", False, "(str) Filename of OUYA Console icon. It must be a 732x412 png image.", '\n'],
    ["android.manifest.intent_filters", "", False, "(str) XML file to include as an intent filters in <activity> tag", '\n'],
    ["android.manifest.launch_mode", "standard", False, "(str) launchMode to set for the main activity", '\n'],
    ["android.add_libs_armeabi", "libs/android/*.so", False, "(list) Android additional libraries to copy into libs/armeabi", ''],
    ["android.add_libs_armeabi_v7a", "libs/android-v7/*.so", False, "", ''],
    ["android.add_libs_arm64_v8a", "libs/android-v8/*.so", False, "", ''],
    ["android.add_libs_x86", "libs/android-x86/*.so", False, "", ''],
    ["android.add_libs_mips", "libs/android-mips/*.so", False, "", '\n'],
    ["android.wakelock", "False", False, (
        "(bool) Indicate whether the screen should stay on\n"
        "Don't forget to add the WAKE_LOCK permission if you set this to True"), '\n'],
    ["android.meta_data", "", False, "(list) Android application meta-data to set (key=value format)", '\n'],
    ["android.library_references", "", False, (
        "(list) Android library project to add (will be added in the\n"
        "project.properties automatically.)"), '\n'],
    ["android.uses_library", "", False, "(list) Android shared libraries which will be added to AndroidManifest.xml using <uses-library> tag", '\n'],
    ["android.logcat_filters", "*:S python:D", False, "(str) Android logcat filters to use", '\n'],
    ["android.logcat_pid_only", "False", False, "(bool) Android logcat only display log for activity's pid", '\n'],
    ["android.adb_args", "-H host.docker.internal", False, "(str) Android additional adb arguments", '\n'],
    ["android.copy_libs", "1", False, "(bool) Copy library instead of making a libpymodules.so", '\n'],
    ["android.archs", "arm64-v8a, armeabi-v7a", True, (
        "(list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64\n"
        "In past, was `android.arch` as we weren't supporting builds for multiple archs at the same time."), '\n'],
    ["android.numeric_version", "1", False, (
        "(int) overrides automatic versionCode computation (used in build.gradle)\n"
        "this is not the same as app version and should only be edited if you know what you're doing"), '\n'],
    ["android.allow_backup", "True", True, "(bool) enables Android auto backup feature (Android API >=23)", '\n'],
    ["android.backup_rules", "", False, "(str) XML file for custom backup rules (see official auto backup documentation)", '\n'],
    ["android.manifest_placeholders", "[:]", False, (
        "(str) If you need to insert variables into your AndroidManifest.xml file,\n"
        "you can do so with the manifestPlaceholders property.\n"
        "This property takes a map of key-value pairs. (via a string)\n"
        "Usage example : android.manifest_placeholders = [myCustomUrl:\"org.kivy.customurl\"]"), '\n'],
    ["android.no-compile-pyo", "True", False, "(bool) disables the compilation of py to pyc/pyo files when packaging", '\n'],
    ["android.release_artifact", "aab", False, "(str) The format used to package the app for release mode (aab or apk or aar).", '\n'],
    ["android.debug_artifact", "apk", False, "(str) The format used to package the app for debug mode (apk or aar).", '\n\n#\n# Python for android (p4a) specific\n#\n'],
    ["p4a.url", "", False, "(str) python-for-android URL to use for checkout", '\n'],
    ["p4a.fork", "kivy", False, "(str) python-for-android fork to use in case if p4a.url is not specified, defaults to upstream (kivy)", '\n'],
    ["p4a.branch", "master", False, "(str) python-for-android branch to use, defaults to master", '\n'],
    ["p4a.commit", "HEAD", False, "(str) python-for-android specific commit to use, defaults to HEAD, must be within p4a.branch", '\n'],
    ["p4a.source_dir", "", False, "(str) python-for-android git clone directory (if empty, it will be automatically cloned from github)", '\n'],
    ["p4a.local_recipes", "", False, "(str) The directory in which python-for-android should look for your own build recipes (if any)", '\n'],
    ["p4a.hook", "", False, "(str) Filename to the hook for p4a", '\n'],
    ["p4a.bootstrap", "sdl2", False, "(str) Bootstrap to use for android builds", '\n'],
    ["p4a.port ", "", False, "(int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)", '\n'],
    ["p4a.setup_py", "false", False, (
        "Control passing the --use-setup-py vs --ignore-setup-py to p4a\n"
        "\"in the future\" --use-setup-py is going to be the default behaviour in p4a, right now it is not\n"
        "Setting this to false will pass --ignore-setup-py, true will pass --use-setup-py\n"
        "NOTE: this is general setuptools integration, having pyproject.toml is enough, no need to generate\n"
        "setup.py if you're using Poetry, but you need to add \"toml\" to source.include_exts."), '\n'],
    ["p4a.extra_args", "", False, "(str) extra command line arguments to pass when invoki-ng -.toolchain", '\n\n#\n# iOS specific\n#\n'],
    ["ios.kivy_ios_dir", "../kivy-ios", False, "(str) Path to a custom kivy-ios folder", '\n'],
    ["ios.kivy_ios_url", "https://github.com/kivy/kivy-ios", True, "Alternately, specify the URL and branch of a git checkout:", ''],
    ["ios.kivy_ios_branch", "master", True, "", '\n'],
    ["ios.ios_deploy_dir", "../ios_deploy", False, (
        "Another platform dependency: ios-deploy\n"
        "Uncomment to use a custom checkout"), '\n'],
    ["ios.ios_deploy_url", "https://github.com/phonegap/ios-deploy", True, "Or specify URL and branch", ''],
    ["ios.ios_deploy_branch", "1.10.0", True, "", '\n'],
    ["ios.codesign.allowed", "false", True, "(bool) Whether or not to sign the code", '\n'],
    ["ios.codesign.debug ", "\"iPhone Developer: <lastname> <firstname> (<hexstring>)\"", False, (
        "(str) Name of the certificate to use for signing the debug version\n"
        "Get a list of available identities: buildozer ios list_identities"), '\n'],
    ["ios.codesign.development_team.debug", "<hexstring>", False, "(str) The development team to use for signing the debug version", '\n'],
    ["ios.codesign.release", "%(ios.codesign.debug)s", False, "(str) Name of the certificate to use for signing the release version", '\n'],
    ["ios.codesign.development_team.release", "<hexstring>", False, "(str) The development team to use for signing the release version", '\n'],
    ["ios.manifest.app_url", "", False, (
        "(str) URL pointing to .ipa file to be installed\n"
        "This option should be defined along with `display_image_url` and `full_size_image_url` options."), '\n'],
    ["ios.manifest.display_image_url", "", False, (
        "(str) URL pointing to an icon (57x57px) to be displayed during download\n"
        "This option should be defined along with `app_url` and `full_size_image_url` options."), '\n'],
    ["ios.manifest.full_size_image_url", "", False, (
        "(str) URL pointing to a large icon (512x512px) to be used by iTunes\n"
        "This option should be defined along with `app_url` and `display_image_url` options."), '\n\n\n[buildozer]\n'],
    ["log_level", "2", True, "(int) Log level (0 = error only, 1 = info, 2 = debug (with command output))", '\n'],
    ["warn_on_root", "1", True, "(int) Display warning if buildozer is run as root (0 = False, 1 = True)", '\n'],
    ["build_dir", "./.buildozer", False, "(str) Path to build artifact storage, absolute or relative to spec file", '\n'],
    ["bin_dir", "./bin", False, "(str) Path to build output (i.e. .apk, .aab, .ipa) storage", '\n'],
]
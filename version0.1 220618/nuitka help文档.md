# nuitka库的help内容  
## 复制至此方便翻译  
Options:
 ###  --version             
show program's version number and exit  
显示程序的版本号并退出  
  ###   -h, --help            
show this help message and exit  
显示此帮助消息并退出  
  ###   --module            
Create an extension module executable instead of a program. Defaults to off.  
创建扩展模块可执行文件，而不是程序。默认为关闭。  
   ###  --standalone       
Enable standalone mode for output. This allows you to transfer the created binary to other machines without it using an existing Python installation. This also means it will become big. It implies these option: "--follow-imports" and "--python-flag=no_site". Defaults to off.  
为输出启用独立模式。这允许您将创建的二进制文件传输到其他机器，而无需使用现有的Python安装。这也意味着它将变得更大。它暗示了以下选项：“--跟随导入”和“-python标志=no\u站点”。默认为关闭。  
  ###   --onefile             
On top of standalone mode, enable onefile mode. This means not a folder, but a compressed executable is created and used. Defaults to off.  
在独立模式之上，启用onefile模式。这意味着创建并使用的不是文件夹，而是压缩的可执行文件。默认为关闭。  
   ###  --python-debug        
Use debug version or not. Default uses what you are using to run Nuitka, most likely a non-debug version.  
是否使用调试版本。默认使用您正在运行的Nuitka，很可能是非调试版本。  
  ###   --python-flag=FLAG    
Python flags to use. Default is what you are using to run Nuitka, this enforces a specific mode. These are options that also exist to standard Python executable. Currently supported: "-S" (alias "no_site"), "static_hashes" (do not use hash randomization), "no_warnings" (do not give Python runtime warnings), -O" (alias "no_asserts"), "no_docstrings" (do not use docstrings), "-u" (alias "unbuffered") and "-m". Default empty.  
要使用的Python标志。默认值是您用来运行Nuitka的，这将强制执行特定模式。这些选项也存在于标准Python可执行文件中。当前支持：“-S”（别名“no_site”）、“static_hashes”（不使用散列随机化）、“no_warnings”（不提供Python运行时警告）、-O”（别名“no_asserts”）、“no_docstrings”（不使用docstrings）、“-u”（别名“unbuffered”）和“-m”。默认为空。  
  ###   --python-for-scons=PATH
If using Python3.3 or Python3.4, provide the path of a Python binary to use for Scons. Otherwise Nuitka can use what you run Nuitka with or a "scons" binary that is found in PATH, or a Python installation from Windows registry.   
如果使用Python3.3或Python3.4，请提供用于SCON的Python二进制文件的路径。否则，Nuitka可以使用运行Nuitka时使用的内容，或者在PATH中找到的“scons”二进制文件，或者使用Windows注册表中的Python安装。  
  ###   --warn-implicit-exceptions
Enable warnings for implicit exceptions detected at compile time.    
为编译时检测到的隐式异常启用警告。  
  ###   --warn-unusual-code   
Enable warnings for unusual code detected at compile time.  
对编译时检测到的异常代码启用警告。  
  ###   --assume-yes-for-downloads  
Allow Nuitka to download external code if necessary, e.g. dependency walker, ccache, and even gcc on Windows. To disable, redirect input from nul device, e.g. "</dev/null" or "<NUL:". Default is to prompt.  
如有必要，允许Nuitka下载外部代码，例如依赖项walker、ccache，甚至Windows上的gcc。要禁用，请重定向来自nul设备的输入，例如“</dev/null”或“<nul：”。默认为提示。  
### Control the inclusion of modules and packages in result.:    
控制结果中模块和包的包含：  
  ###   --include-package=PACKAGE  
Include a whole package. Give as a Python namespace, e.g. "some_package.sub_package" and Nuitka will then find it and include it and all the modules found below that disk location in the binary or extension module it creates, and make it available for import by the code. To avoid unwanted sub packages, e.g. tests you can e.g. do this "--nofollow-import-to=*.tests". Default empty.  
包括整个包装。以Python名称空间的形式给出，例如“some_package.sub_package”，然后Nuitka将找到它，并将它和在该磁盘位置下找到的所有模块包含在它创建的二进制或扩展模块中，并使其可供代码导入。为了避免不需要的子包，例如测试，您可以这样做“-nofollow import To=*.tests”。默认为空。  
  ###   --include-module=MODULE  
Include a single module. Give as a Python namespace, e.g. "some_package.some_module" and Nuitka will then find it and include it in the binary or extension module it creates, and make it available for import by the code. Default empty.   
包括单个模块。以Python名称空间的形式给出，例如“some\u package.some\u module”，然后Nuitka将找到它并将其包含在它创建的二进制或扩展模块中，并使其可供代码导入。默认为空。  
  ###    --include-plugin-directory=MODULE/PACKAGE  
Include the content of that directory, no matter if it's used by the given main program in a visible form. Overrides all other inclusion options. Can be given multiple times. Default empty.  
包括该目录的内容，无论给定主程序是否以可见形式使用该目录。替代所有其他包含选项。可以多次给出。默认为空。  
  ###   --include-plugin-files=PATTERN   
Include into files matching the PATTERN. Overrides all other follow options. Can be given multiple times. Default empty.  
包含到与模式匹配的文件中。替代所有其他跟随选项。可以多次给出。默认为空。  
  ###   --prefer-source-code  
For already compiled extension modules, where there is both a source file and an extension module, normally the extension module is used, but it should be better to compile the module from available source code for best performance. If not desired, there is --no-prefer-source-code to disable warnings about it. Default off.  
对于已经编译的扩展模块，如果既有源文件又有扩展模块，通常会使用扩展模块，但最好从可用的源代码编译模块以获得最佳性能。如果不需要，则没有首选源代码来禁用有关它的警告。默认关闭。  
## Control the following into imported modules:  
将以下内容控制到导入的模块中：  
  ###   --follow-stdlib     
Also descend into imported modules from standard library. This will increase the compilation time by a lot. Defaults to off.  
也可以从标准库下降到导入的模块中。这将大大增加编译时间。默认为关闭。  
  ###   --nofollow-imports    
When --nofollow-imports is used, do not descend into any imported modules at all, overrides all other inclusion options. Defaults to off.  
当使用--nofollow-imports时，根本不要进入任何导入的模块，会覆盖所有其他包含选项。默认为关闭。  
  ###   --follow-imports    
When --follow-imports is used, attempt to descend into all imported modules. Defaults to off.  
使用--follow imports时，尝试进入所有导入的模块。默认为关闭。  
  ###   --follow-import-to=MODULE/PACKAGE  
Follow to that module if used, or if a package, to the  whole package. Can be given multiple times. Default empty.  
如果使用了该模块，请遵循该模块；如果是一个包，请遵循整个包。可以多次给出。默认为空。  
  ###   --nofollow-import-to=MODULE/PACKAGE  
Do not follow to that module name even if used, or if a package name, to the whole package in any case, overrides all other options. Can be given multiple times. Default empty.  
即使使用了该模块名，也不要使用该模块名，或者如果某个包名，则在任何情况下都不要使用整个包，否则会覆盖所有其他选项。可以多次给出。默认为空。  
## Data files for standalone/onefile mode:  
独立/单一文件模式的数据文件：  
  ###   --include-package-data=PACKAGE  
Include data files of the given package name. Can use patterns. By default Nuitka does not unless hard coded and vital for operation of a package. This will include all non-DLL, non-extension modules in the distribution. Default empty.  
包括给定包名称的数据文件。可以使用模式。默认情况下，Nuitka不会这样做，除非是硬编码的，并且对于包的操作至关重要。这将包括发行版中的所有非DLL、非扩展模块。默认为空。  
  ###   --include-data-files=DESC  
Include data files by filenames in the distribution. There are many allowed forms. With '--include-data-files=/path/to/file/*.txt=folder_name/some.txt' it will copy a single file and complain if it's multiple. With '--include-data-files=/path/to/files/*.txt=folder_name/' it will put all matching files into that folder. For recursive copy there is a form with 3 values that '--include-data-files=/path/to/scan=folder_name=**/*.txt' that will preserve directory structure. Default empty.    
在分发中按文件名包括数据文件。有许多允许的形式。带"--include-data-files=/path/to/file/*.txt=folder_name/some.txt"它将复制一个文件，如果有多个文件，则会进行投诉。带"--include-data-files=/path/to/files/*.txt=folder_name/"它会将所有匹配的文件放入该文件夹。对于递归复制，有一个具有3个值的表单，该值为"--include-data-files=/path/to/scan=folder_name=**/*.txt"，将保留目录结构。默认为空。  
  ###   --include-data-dir=DIRECTORY  
Include data files from complete directory in the distribution. This is recursive. Check '--include-data-files' with patterns if you want non-recursive inclusion. An example would be '--include-data-dir=/path/somedir=data/somedir' for plain copy, of the whole directory. All files are copied, if you want to exclude files you need to remove them beforehand, or use --noinclude-data-files option to remove them. Default empty.  
在发行版中包含完整目录中的数据文件。这是递归的。如果希望非递归包含，请选中带模式的“--包含数据文件”。对于整个目录的纯拷贝，例如“--include data dir=/path/somedir=data/somedir”。所有文件都会被复制，如果要排除文件，需要事先删除它们，或者使用--noinclude data files选项删除它们。默认为空。  
  ###   --noinclude-data-files=PATTERN  
                        Do not include data files matching the filename pattern given. This is against the target filename, not source paths. So ignore file pattern from package data for "package_name" should be matched as "package_name/*.txt". Default empty.    
不要包含与给定文件名模式匹配的数据文件。这是针对目标文件名，而不是源路径。因此，“package_name”的“ignore file pattern from package data”应匹配为"package_name/*.txt"。默认为空。  

## Immediate execution after compilation:    
编译后立即执行：  
  ###   --run               
Execute immediately the created binary (or import the compiled module). Defaults to off.  
立即执行创建的二进制文件（或导入已编译的模块）。默认为关闭。  
  ###   --debugger, --gdb   
Execute inside a debugger, e.g. "gdb" or "lldb" to automatically get a stack trace. Defaults to off.  
在调试器内执行，例如“gdb”或“lldb”，以自动获取堆栈跟踪。默认为关闭。  
  ###   --execute-with-pythonpath  
                        When immediately executing the created binary(--execute), don't reset PYTHONPATH. When all modules are successfully included, you ought to not need PYTHONPATH anymore.  
当立即执行创建的二进制文件（-execute）时，不要重置PYTHONPATH。成功包含所有模块后，您应该不再需要PYTHONPATH了。  
## Dump options for internal tree:  
内部树的转储选项：  
  ###   --xml               
Dump the final result of optimization as XML, then exit.  
将优化的最终结果转储为XML，然后退出。  
## Code generation choices:  
代码生成选项：  
  ###   --disable-bytecode-cache  
                        Do not reuse dependency analysis results for modules, esp. from standard library, that are included as bytecode.  
不要重用模块的依赖关系分析结果，尤其是来自标准库的依赖关系分析结果，这些模块包含在字节码中。  
  ###   --full-compat       
Enforce absolute compatibility with CPython. Do not even allow minor deviations from CPython behavior, e.g. not having better tracebacks or exception messages which are not really incompatible, but only different. This is intended for tests only and should not be used for normal use.  
强制与CPython绝对兼容。甚至不允许与CPython行为有细微的偏差，例如没有更好的回溯或异常消息，这些消息并非真正不兼容，只是不同而已。这仅用于测试，不应用于正常使用。  
  ###   --file-reference-choice=MODE  
                        Select what value "__file__" is going to be. With "runtime" (default for standalone binary mode and module mode), the created binaries and modules, use the location of themselves to deduct the value of  "__file__". Included packages pretend to be in directories below that location. This allows you to include data files in deployments. If you merely seek acceleration, it's better for you to use the "original" value, where the source files location will be used. With "frozen" a notation "<frozen module_name>" is used. For compatibility reasons, the "__file__" value will always have ".py" suffix independent of what it really is.  
选择"__file__"的值。使用“runtime”（独立二进制模式和模块模式的默认值），创建的二进制文件和模块使用其自身的位置来扣除"__file__"。包含的包假装位于该位置下方的目录中。这允许您在展开中包括数据文件。如果只是寻求加速，最好使用“原始”值，即使用源文件位置的位置。对于“冻结”，使用符号“<frozen module_name>”。出于兼容性原因，"__file__".
  ###    --module-name-choice=MODE  
                        Select what value "__name__" and "__package__" are going to be. With "runtime" (default for module mode), the created module uses the parent package to deduce the value of "__package__", to be fully compatible. The value "original" (default for other modes) allows for more static optimization to happen, but is incompatible for modules that normally can be loaded into any package.  
选择"__name__"和 "__package__" 。对于“runtime”（模块模式的默认值），创建的模块使用父包推断"__package__"。值“original”（其他模式的默认值）允许进行更多的静态优化，但与通常可以加载到任何包中的模块不兼容。
## Output choices:  
  ###   -o FILENAME    
     Specify how the executable should be named. For extension modules there is no choice, also not for  standalone mode and using it will be an error. This may include path information that needs to exist though. Defaults to '<program_name>' on this platform..exe  
指定可执行文件的命名方式。对于扩展模块，没有选择，也没有独立模式，使用它将是一个错误。这可能包括需要存在的路径信息。此平台上的默认值为"<program_name>"..exe文件  
  ###   --output-dir=DIRECTORY  
                        Specify where intermediate and final output files should be put. The DIRECTORY will be populated with C files, object files, etc. Defaults to current directory.  
指定中间和最终输出文件的放置位置。该目录将填充C文件、对象文件等。默认为当前目录。  
  ###   --remove-output      
Removes the build directory after producing the module or exe file. Defaults to off.  
生成模块或exe文件后删除生成目录。默认为关闭。  
  ###   --no-pyi-file       
Do not create a ".pyi" file for extension modules created by Nuitka. This is used to detect implicit imports. Defaults to off.  
不要为Nuitka创建的扩展模块创建“.pyi”文件。这用于检测隐式导入。默认为关闭。  

  Debug features:
    --debug             Executing all self checks possible to find errors in
                        Nuitka, do not use for production. Defaults to off.
    --unstriped         Keep debug info in the resulting object file for
                        better debugger interaction. Defaults to off.
    --profile           Enable vmprof based profiling of time spent. Not
                        working currently. Defaults to off.
    --internal-graph    Create graph of optimization process internals, do not
                        use for whole programs, but only for small test cases.
                        Defaults to off.
    --trace-execution   Traced execution output, output the line of code
                        before executing it. Defaults to off.
    --recompile-c-only  This is not incremental compilation, but for Nuitka
                        development only. Takes existing files and simply
                        compile them as C again. Allows compiling edited C
                        files for quick debugging changes to the generated
                        source, e.g. to see if code is passed by, values
                        output, etc, Defaults to off. Depends on compiling
                        Python source to determine which files it should look
                        at.
    --generate-c-only   Generate only C source code, and do not compile it to
                        binary or module. This is for debugging and code
                        coverage analysis that doesn't waste CPU. Defaults to
                        off. Do not think you can use this directly.
    --experimental=FLAG
                        Use features declared as 'experimental'. May have no
                        effect if no experimental features are present in the
                        code. Uses secret tags (check source) per experimented
                        feature.
    --low-memory        Attempt to use less memory, by forking less C
                        compilation jobs and using options that use less
                        memory. For use on embedded machines. Use this in case
                        of out of memory problems. Defaults to off.
    --disable-dll-dependency-cache
                        Disable the dependency walker cache. Will result in
                        much longer times to create the distribution folder,
                        but might be used in case the cache is suspect to
                        cause errors.
    --force-dll-dependency-cache-update
                        For an update of the dependency walker cache. Will
                        result in much longer times to create the distribution
                        folder, but might be used in case the cache is suspect
                        to cause errors or known to need an update.

  Backend C compiler choice:
    --clang             Enforce the use of clang. On Windows this requires a
                        working Visual Studio version to piggy back on.
                        Defaults to off.
    --mingw64           Enforce the use of MinGW64 on Windows. Defaults to
                        off.
    --msvc=MSVC_VERSION
                        Enforce the use of specific MSVC version on Windows.
                        Allowed values are e.g. "14.3" (MSVC 2022) and other
                        MSVC version numbers, specify "list" for a list of
                        installed compilers, or use "latest".  Defaults to
                        latest MSVC being used if installed, otherwise MinGW64
                        is used.
    -j N, --jobs=N      Specify the allowed number of parallel C compiler
                        jobs. Defaults to the system CPU count.
    --lto=choice        Use link time optimizations (MSVC, gcc, clang).
                        Allowed values are "yes", "no", and "auto" (when it's
                        known to work). Defaults to "auto".
    --static-libpython=choice
                        Use static link library of Python. Allowed values are
                        "yes", "no", and "auto" (when it's known to work).
                        Defaults to "auto".
    --disable-ccache    Do not attempt to use ccache (gcc, clang, etc.) or
                        clcache (MSVC, clangcl).

  PGO compilation choices:
    --pgo               Enables C level profile guided optimization (PGO), by
                        executing a dedicated build first for a profiling run,
                        and then using the result to feedback into the C
                        compilation. Note: This is experimental and not
                        working with standalone modes of Nuitka yet. Defaults
                        to off.
    --pgo-args=PGO_ARGS
                        Arguments to be passed in case of profile guided
                        optimization. These are passed to the special built
                        executable during the PGO profiling run. Default
                        empty.
    --pgo-executable=PGO_EXECUTABLE
                        Command to execute when collecting profile
                        information. Use this only, if you need to launch it
                        through a script that prepares it to run. Default use
                        created program.

  Tracing features:
    --quiet             Disable all information outputs, but show warnings.
                        Defaults to off.
    --show-scons        Operate Scons in non-quiet mode, showing the executed
                        commands. Defaults to off.
    --show-progress     Provide progress information and statistics. Defaults
                        to off.
    --no-progressbar    Disable progress bar outputs (if tqdm is installed).
                        Defaults to off.
    --show-memory       Provide memory information and statistics. Defaults to
                        off.
    --show-modules      Provide information for included modules and DLLs
                        Defaults to off.
    --show-modules-output=PATH
                        Where to output --show-modules, should be a filename.
                        Default is standard output.
    --report=COMPILATION_REPORT_FILENAME
                        Report module inclusion in an XML output file. Default
                        is off.
    --verbose           Output details of actions taken, esp. in
                        optimizations. Can become a lot. Defaults to off.
    --verbose-output=PATH
                        Where to output --verbose, should be a filename.
                        Default is standard output.

  General OS controls:
    --disable-console, --macos-disable-console, --windows-disable-console
                        When compiling for Windows or macOS, disable the
                        console window and create a GUI application. Defaults
                        to off.
    --enable-console    When compiling for Windows or macOS, enable the
                        console window and create a console application. This
                        disables hints from certain modules, e.g. "PySide"
                        that suggest to disable it. Defaults to true.
    --force-stdout-spec=FORCE_STDOUT_SPEC, --windows-force-stdout-spec=FORCE_STDOUT_SPEC
                        Force standard output of the program to go to this
                        location. Useful for programs with disabled console
                        and programs using the Windows Services Plugin of
                        Nuitka commercial. Defaults to not active, use e.g.
                        '%PROGRAM%.out.txt', i.e. file near your program.
    --force-stderr-spec=FORCE_STDERR_SPEC, --windows-force-stderr-spec=FORCE_STDERR_SPEC
                        Force standard error of the program to go to this
                        location. Useful for programs with disabled console
                        and programs using the Windows Services Plugin of
                        Nuitka commercial. Defaults to not active, use e.g.
                        '%PROGRAM%.err.txt', i.e. file near your program.

  Windows specific controls:
    --windows-icon-from-ico=ICON_PATH
                        Add executable icon. Can be given multiple times for
                        different resolutions or files with multiple icons
                        inside. In the later case, you may also suffix with
                        #<n> where n is an integer index starting from 1,
                        specifying a specific icon to be included, and all
                        others to be ignored.
    --windows-icon-from-exe=ICON_EXE_PATH
                        Copy executable icons from this existing executable
                        (Windows only).
    --onefile-windows-splash-screen-image=SPLASH_SCREEN_IMAGE
                        When compiling for Windows and onefile, show this
                        while loading the application. Defaults to off.
    --windows-uac-admin
                        Request Windows User Control, to grant admin rights on
                        execution. (Windows only). Defaults to off.
    --windows-uac-uiaccess
                        Request Windows User Control, to enforce running from
                        a few folders only, remote desktop access. (Windows
                        only). Defaults to off.
    --windows-company-name=WINDOWS_COMPANY_NAME
                        Name of the company to use in Windows Version
                        information.  One of file or product version is
                        required, when a version resource needs to be added,
                        e.g. to specify product name, or company name.
                        Defaults to unused.
    --windows-product-name=WINDOWS_PRODUCT_NAME
                        Name of the product to use in Windows Version
                        information. Defaults to base filename of the binary.
    --windows-file-version=WINDOWS_FILE_VERSION
                        File version to use in Windows Version information.
                        Must be a sequence of up to 4 numbers, e.g. 1.0.0.0,
                        only this format is allowed. One of file or product
                        version is required, when a version resource needs to
                        be added, e.g. to specify product name, or company
                        name. Defaults to unused.
    --windows-product-version=WINDOWS_PRODUCT_VERSION
                        Product version to use in Windows Version information.
                        Must be a sequence of up to 4 numbers, e.g. 1.0.0.0,
                        only this format is allowed. One of file or product
                        version is required, when a version resource needs to
                        be added, e.g. to specify product name, or company
                        name. Defaults to unused.
    --windows-file-description=WINDOWS_FILE_DESCRIPTION
                        Description of the file use in Windows Version
                        information.  One of file or product version is
                        required, when a version resource needs to be added,
                        e.g. to specify product name, or company name.
                        Defaults to nonsense.
    --windows-onefile-tempdir-spec=ONEFILE_TEMPDIR_SPEC, --onefile-tempdir-spec=ONEFILE_TEMPDIR_SPEC
                        Use this as a temporary folder. Defaults to
                        '%TEMP%\onefile_%PID%_%TIME%', i.e. system temporary
                        directory.

  macOS specific controls:
    --macos-target-arch=MACOS_TARGET_ARCH
                        What architectures is this to supposed to run on.
                        Default and limit is what the running Python allows
                        for. Default is "native" which is the architecture the
                        Python is run with.
    --macos-create-app-bundle
                        When compiling for macOS, create a bundle rather than
                        a plain binary application. Currently experimental and
                        incomplete. Currently this is the only way to unlock
                        disabling of console.Defaults to off.
    --macos-app-icon=ICON_PATH
                        Add icon for the application bundle to use. Can be
                        given only one time. Defaults to Python icon if
                        available.
    --macos-signed-app-name=MACOS_SIGNED_APP_NAME
                        Name of the application to use for macOS signing.
                        Follow "com.yourcompany.appname" naming results for
                        best results, as these have to be globally unique, and
                        will potentially grant protected API accesses.
    --macos-app-name=MACOS_APP_NAME
                        Name of the product to use in macOS bundle
                        information. Defaults to base filename of the binary.
    --macos-sign-identity=MACOS_APP_VERSION
                        When signing on macOS, by default an ad-hoc identify
                        will be used, but with this option your get to specify
                        another identity to use. The signing of code is now
                        mandatory on macOS and cannot be disabled. Default "-"
                        if not given, which means ad-hoc.
    --macos-app-version=MACOS_APP_VERSION
                        Product version to use in macOS bundle information.
                        Defaults to "1.0" if not given.
    --macos-app-protected-resource=RESOURCE_DESC
                        Request access for macOS protected resources, e.g.
                        "NSMicrophoneUsageDescription:Microphone access for
                        recording audio." requests access to the microphone
                        and provides an informative text for the user, why
                        that is needed. Before the colon, is an OS identifier
                        for an access right, then the informative text. Legal
                        values can be found on https://developer.apple.com/doc
                        umentation/bundleresources/information_property_list/p
                        rotected_resources and the option can be specified
                        multiple times. Default empty.

  Linux specific controls:
    --linux-onefile-icon=ICON_PATH
                        Add executable icon for onefile binary to use. Can be
                        given only one time. Defaults to Python icon if
                        available.
    --linux-onefile-compression=COMPRESSION
                        Compression method to use for Linux onefile builds.
                        Defaults to gzip for faster decompression

  Plugin control:
    --enable-plugin=PLUGIN_NAME, --plugin-enable=PLUGIN_NAME
                        Enabled plugins. Must be plug-in names. Use --plugin-
                        list to query the full list and exit. Default empty.
    --disable-plugin=PLUGIN_NAME, --plugin-disable=PLUGIN_NAME
                        Disabled plugins. Must be plug-in names. Use --plugin-
                        list to query the full list and exit. Default empty.
    --plugin-no-detection
                        Plugins can detect if they might be used, and the you
                        can disable the warning via "--disable-plugin=plugin-
                        that-warned", or you can use this option to disable
                        the mechanism entirely, which also speeds up
                        compilation slightly of course as this detection code
                        is run in vain once you are certain of which plugins
                        to use. Defaults to off.
    --plugin-list       Show list of all available plugins and exit. Defaults
                        to off.
    --user-plugin=PATH  The file name of user plugin. Can be given multiple
                        times. Default empty.
    --show-source-changes
                        Show source changes to original Python file content
                        before compilation. Mostly intended for developing
                        plugins. Default False.

  Plugin anti-bloat:
    --show-anti-bloat-changes
                        Annotate what changes are by the plugin done.
    --noinclude-setuptools-mode=NOINCLUDE_SETUPTOOLS_MODE
                        What to do if a setuptools import is encountered. This
                        package can be big with dependencies, and should
                        definitely be avoided.
    --noinclude-pytest-mode=NOINCLUDE_PYTEST_MODE
                        What to do if a pytest import is encountered. This
                        package can be big with dependencies, and should
                        definitely be avoided.
    --noinclude-unittest-mode=NOINCLUDE_UNITTEST_MODE
                        What to do if a unittest import is encountered. This
                        package can be big with dependencies, and should
                        definitely be avoided.
    --noinclude-IPython-mode=NOINCLUDE_IPYTHON_MODE
                        What to do if a IPython import is encountered. This
                        package can be big with dependencies, and should
                        definitely be avoided.
    --noinclude-default-mode=NOINCLUDE_DEFAULT_MODE
                        This actually provides the default "warning" value for
                        above options, and can be used to turn all of these
                        on.
    --noinclude-custom-mode=CUSTOM_CHOICES
                        What to do if a specific import is encountered. Format
                        is module name, which can and should be a top level
                        package and then one choice, "error", "warning",
                        "nofollow", e.g. PyQt5:error.

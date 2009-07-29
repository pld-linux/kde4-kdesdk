#
# TODO:
# - do something with /usr/share/apps/kdevappwizard/template_previews/
# - add man files
#
%define		_state		stable
%define		orgname		kdesdk
%define		qtver		4.5.0

Summary:	KDESDK - Software Development Kit for KDE
Summary(pl.UTF-8):	KDESDK - Wsparcie programistyczne dla KDE
Name:		kde4-kdesdk
Version:	4.3.0
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	eda2376a54d66899bf7beb60cc0843b1
#Patch100:	%{name}-branch.diff
Patch0:		%{name}-kiosvn.patch
URL:		http://www.kde.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtDesigner-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtUiTools-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	binutils-devel
BuildRequires:	bison
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.6.3
BuildRequires:	db-devel
BuildRequires:	emacs-common
BuildRequires:	flex
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	kde4-kdepim-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	giflib-devel
BuildRequires:	libltdl-devel
BuildRequires:	libjpeg-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	perl-tools-pod
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	strigi-devel >= 0.6.3
BuildRequires:	subversion-devel >= 0.37.0
BuildRequires:	utempter-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gimpdir	%(gimptool --gimpdatadir 2>/dev/null)
%define		_appdefsdir	%{_datadir}/X11/app-defaults
%define		_emacspkgdir	/usr/share/emacs/%(rpm -q --qf %{V} emacs-common | tr -d '[a-z]')
%define		_xemacspkgdir	/usr/share/xemacs-packages
%define		_zshfcdir	/usr/share/zsh/latest/functions

%description
Software Development Kit for KDE.

%description -l pl.UTF-8
Pakiet wspomagający programowanie w środowisku KDE.

%package kfile
Summary:	Developers' file formats enhanced information
Summary(pl.UTF-8):	Rozszerzone informacje o plikach używanych przez programistów
Group:		X11/Development/Libraries
Requires:	kde4-konqueror >= %{version}

%description kfile
This package adds a tab to konqueror "file properties" dialog window
with file enhanced informations for C++ source files, diff files,
gettext and designer translation sourcefiles.

%description kfile -l pl.UTF-8
Ten pakiet dodaje do okna dialogowego "właściwości pliku" konquerora
dodatkową zakładkę z rozszerzonymi informacjami o pliku.

%package cervisia
Summary:	A KDE CVS frontend
Summary(pl.UTF-8):	Frontend do CVS dla KDE
Group:		X11/Development/Tools
#Requires:	%{name}-libcvsservice = %{version}-%{release}
Requires:	cvs-client >= 1.10
Requires:	kde4-kdebase >= %{version}

%description cervisia
A KDE CVS frontend. It features:
- updating or retrieving the status of a working directory or single
  files. Files are displayed in different colors depending on their
  status, and the shown files can be filtered according to their status
- common operations like adding, removing and commiting files.
- advanced operations like adding and removing watches, editing and
  unediting files, locking and unlocking.
- checking out and importing modules.
- graphical diff against the repository and between different
  revisions.
- blame-annotated view of a file.
- view of the log messages in tree and list form.
- resolving of conflicts in a file.
- tagging and branching.
- updating to a tag, branch or date.
- a Changelog editor coupled with the commit dialog.

%description cervisia -l pl.UTF-8
Frontend do CVS dla KDE. Ma następujące możliwości:
- uaktualnianie lub odtwarzanie stanu katalogu lub pojedynczych
  plików; pliki są wyświetlane w różnych kolorach zależnie od ich stanu,
  a pokazywane pliki mogą być filtrowane według ich stanu
- podstawowe operacje, takie jak dodawanie, usuwanie i commitowanie
  plików
- zaawansowane operacje, takie jak dodawanie i usuwanie śledzenia,
  włączanie i wyłączanie edycji plików, blokowanie i odblokowywanie
- pobieranie i importowanie modułów
- graficzne wyświetlanie różnic względem repozytorium i między różnymi
  rewizjami
- widok pliku opisany winnymi
- widok loga komentarzy do zmian w postaci drzewa i listy
- rozwiązywanie konfliktów w pliku
- tagowanie i branchowanie
- uaktualnianie do taga, brancha lub daty
- edytor changelogów połączony z oknem dialogowym do commitowania.

%package completions-bash
Summary:	Autocomplete definitions for bash
Summary(pl.UTF-8):	Definicje autouzupełniania dla basha
Group:		Applications/Shells
Requires:	bash-completion

%description completions-bash
Autocomplete definitions for bash.

%description completions-bash -l pl.UTF-8
Definicje autouzupełniania dla basha.

%package completions-zsh
Summary:	Autocomplete definitions for zsh
Summary(pl.UTF-8):	Definicje autouzupełniania dla zsh
Group:		Applications/Shells
Requires:	zsh >= 4.0.6-2

%description completions-zsh
Autocomplete definitions for zsh.

%description completions-zsh -l pl.UTF-8
Definicje autouzupełniania dla zsh.

%package lokalize
Summary:	Computer-aided translation system that focuses on productivity and performance
Summary(pl.UTF-8):	a
Group:		X11/Development/Tools

%description lokalize
Lokalize is a computer-aided translation system that focuses on
productivity and performance. Translator does only creative work (of
delivering message in his/her mother language in laconic and easy to
understand form). Lokalize implies parapgraph-by-paragrah translation
approach (when translating documentation) and message-by-message
approach (when translating GUI).

%description lokalize -l pl.UTF-8
a

%package kde-resource-kdeaccounts
Summary:	A kdeaccounts plugin for the KDE PIM framework
Summary(pl.UTF-8):	Wtyczka do książki adresowej KDE dodająca obsługę kdeaccounts
Group:		X11/Applications
Requires:	kde4-kdepim-kaddressbook >= %{version}

%description kde-resource-kdeaccounts
A kdeaccounts plugin for the KDE adressbook. It allows adding the
people from KDE's CVS accounts file to the addressbook.

%description kde-resource-kdeaccounts -l pl.UTF-8
Wtyczka do książki adresowej KDE dodająca obsługę kdeaccounts. Dodaje
ona osoby posiadające konta w CVS KDE do książki adresowej.

%package kde-resource-bugzilla
Summary:	A bugzilla plugin for the KDE PIM framework
Summary(pl.UTF-8):	Wtyczka do książki adresowej KDE dodająca obsługę bugzilli
Group:		X11/Applications
Requires:	kde4-kdepim-kaddressbook >= %{version}

%description kde-resource-bugzilla
A KDE PIM plugin that allows creating bugzilla TODO lists.

%description kde-resource-bugzilla -l pl.UTF-8
Wtyczka KDE PIM umożliwiająca tworzenie list TODO w bugzilli.

%package kapptemplate
Summary:	KDE application framework generator
Summary(pl.UTF-8):	Generator szkieletu dla aplikacji KDE
Group:		X11/Development/Tools

%description kapptemplate
Modular shell script that will automatically create a framework for
either a normal KDE 3.x application, a KPart application, a KPart
plugin, or convert an existing application.

%description kapptemplate -l pl.UTF-8
Modularny skrypt, który potrafi automatycznie wygenerować szkielet
katalogów dla zwykłej aplikacji pod KDE 3.x, aplikacji KPart, wtyczki
KPart lub skonwertować istniejącą aplikację.

%package kbugbuster
Summary:	A tools that allows cooperation with bugs.kde.org
Summary(pl.UTF-8):	Narzędzie współpracujące z bugs.kde.org
Group:		X11/Development/Tools

%description kbugbuster
KBugBuster allows for easy bug management on bugs.kde.org.

%description kbugbuster -l pl.UTF-8
KBugBuster ułatwia wyszukiwanie i zarządzanie błędami na bugs.kde.org.

%package kcachegrind
Summary:	KCachegrind - visualization of traces generated by profiling
Summary(pl.UTF-8):	KCachegrind - wizualizacja ścieżek tworzonych przez profilowanie
Group:		X11/Development/Tools

%description kcachegrind
KCachegrind visualizes traces generated by profiling.

%description kcachegrind -l pl.UTF-8
KCachegrind wizualizuje ścieżki tworzone przez profilowanie.

%package kmtrace
Summary:	A mtrace to full backtrace conversion tool
Summary(pl.UTF-8):	Narzędzie do konwersji z mtrace do pełnego backtrace'a
Group:		X11/Development/Tools

%description kmtrace
kmtrace converts glibc's mtrace log into a full backtrace.

%description kmtrace -l pl.UTF-8
kmtrace konwertuje mtrace glibca do pełnego backtrace'a.

%package kompare
Summary:	Kompare - a program to view the differences between files
Summary(pl.UTF-8):	Kompare - program służący do porównywania zmian między plikami
Group:		X11/Development/Tools

%description kompare
Kompare is a program to view the differences between files. Features
include:

  - comparison of files or directories via a graphical interface
  - bezier-based connection widget lets you see both source and
    destination as they really appear
  - graphical viewing of patch files in normal, context, unified and
    diff formats
  - interactive application of differences
  - full network transparency
  - ability to view plain-text diff output in embedded viewer
  - easy navigation of multiple-file diffs with dockable navigation tree
  - graphical interface to commonly used diff command line options
  - switch source and destination with one command
  - diff statistics

%description kompare -l pl.UTF-8
Kompare to program służący do porównywania zmian między plikami.
Aktualnie dostępne funkcje:
  - porównanie plików lub katalogów poprzez graficzny interfejs
  - przedstawienie źródła i celu za pomocą krzywej Beziera
  - graficzne przeglądanie łat w formatach diff, unidiff, context i
    zwykłym
  - interaktywne wprowadzanie zmian
  - przezroczystość sieciowa
  - możliwość oglądania wyjścia diff w wewnętrznej przeglądarce
  - łatwa nawigacja między wieloplikowymi diffami wraz z dokowalnym
    drzewem
  - zamiana źródła i celu za pomocą pojedynczej komendy
  - statystyki diffów

%package kprofilemethod
Summary:	Kprofilemethod - a set of macros which help profiling using QTime
Summary(pl.UTF-8):	Kprofilemethod - zestaw makr ułatwiających profilowanie z wykorzystaniem QTime
Group:		X11/Development/Tools

%description kprofilemethod
Kprofilemethod is a set of macros which help profiling using QTime.

%description kprofilemethod -l pl.UTF-8
Kprofilemethod to zestaw makr ułatwiających profilowanie z
wykorzystaniem QTime.

%package kspy
Summary:	A utility for egzamining the internal state of a Qt/KDE application
Summary(pl.UTF-8):	Narzędzie do badania stanu aplikacji Qt/KDE
Group:		X11/Development/Tools

%description kspy
KSpy is a utility intended to help developers examine the internal
state of a Qt/KDE application. KSpy graphically displays all the
QObjects in use, and allows you to browse their properties. Using KSpy
is very simple, include kspy.h and call KSpy::invoke() when you want
to look inside your app. The KSpy function is inline and the main part
of KSpy is dynamically loaded, so you may even want to leave this in
the release build of an application.

%description kspy -l pl.UTF-8
KSpy to narzędzie mające ułatwić programistom badanie wewnętrznego
stanu aplikacji Qt/KDE. KSpy ilustruje graficznie wszystkie QObjects
jakie są w użyciu i pozwala na łatwe przeglądanie ich właściwości.
Korzystanie z KSpy jest bardzo proste (wystarczy dołączyć plik kspy.h
i wywołać KSpy::invoke() w miejscu, które chcemy obejrzeć w naszej
aplikacji. Funkcja KSpy jest inline, więc można zostawić ją nawet w
wydaniu stabilnym.

%package kstartperf
Summary:	A tool to measure startup time for KDE applications
Summary(pl.UTF-8):	Narzędzie służące do pomiaru czasu ładowania aplikacji KDE
Group:		X11/Development/Tools

%description kstartperf
kstartperf measures startup time for KDE applications.

%description kstartperf -l pl.UTF-8
Narzędzie służące do pomiaru czasu ładowania aplikacji KDE.

%package kuiviewer
Summary:	Qt Designer UI file Viewer
Summary(pl.UTF-8):	Przeglądarka plików UI generowanych przez Qt designera
Group:		X11/Development/Tools

%description kuiviewer
Qt Designer UI file Viewer.

%description kuiviewer -l pl.UTF-8
Przeglądarka plików UI generowanych przez Qt designera.

%package kunittest
Summary:	KUnit Test
Summary(pl.UTF-8):	Narzędzie testujące KUnit
Group:		X11/Development/Tools

%description kunittest
KUnit Test.

%description kunittest -l pl.UTF-8
Narzędzie testujące KUnit.

%package libcvsservice
Summary:	A cvs access library
Summary(pl.UTF-8):	Biblioteka dostępu do cvs
Group:		X11/Libraries
Requires:	kde4-kdelibs >= %{version}

%description libcvsservice
A library for access to CVS repositories for KDE apps.

%description libcvsservice -l pl.UTF-8
Biblioteka służąca do kontroli repozytoriów CVS z poziomu aplikacji
KDE.

%package libcvsservice-devel
Summary:	A cvsservice library - header files
Summary(pl.UTF-8):	Biblioteka cvsservice - pliki nagłówkowe
Group:		X11/Development/Libraries
Requires:	%{name}-libcvsservice = %{version}-%{release}

%description libcvsservice-devel
A cvsservice library - header files.

%description libcvsservice-devel -l pl.UTF-8
Biblioteka cvsservice - pliki nagłówkowe.

%package palette-gimp
Summary:	Package which adds the KDE Default palette to GIMP
Summary(pl.UTF-8):	Pakiet dodający domyślną paletę kolorów KDE do GIMP-a
Group:		X11/Applications/Graphics
Requires:	gimp

%description palette-gimp
This package adds the KDE Default palette to GIMP.

%description palette-gimp -l pl.UTF-8
Pakiet dodający domyślną paletę kolorów KDE do GIMP-a.

%package palette-xpaint
Summary:	Package which adds the KDE Default palette to XPaint
Summary(pl.UTF-8):	Pakiet dodający domyślną paletę kolorów KDE do XPainta
Group:		X11/Applications/Graphics
Requires:	xorg-lib-libXt >= 1.0
Requires:	xpaint

%description palette-xpaint
This package adds the KDE Default palette to XPaint.

%description palette-xpaint -l pl.UTF-8
Pakiet dodający domyślną paletę kolorów KDE do XPainta.

%package po2xml
Summary:	An xml2po and vice versa converters
Summary(pl.UTF-8):	Konwertery po2xml i vice versa
Group:		X11/Development/Tools
Requires:	/usr/bin/python

%description po2xml
An xml2po and vice versa converters.

%description po2xml -l pl.UTF-8
Konwertery po2xml i vice versa.

%package scripts-developer
Summary:	An set of scripts useful for building and maintaining KDE
Summary(pl.UTF-8):	Zestaw skryptów do kompilowania i utrzymywania KDE
Group:		X11/Development/Tools
Requires:	/usr/bin/perl

%description scripts-developer
This package contains:
- script that extracts strings in an application's .rc file, e.g.
  testappui.rc, and writes into the pot file
- script that counts lines of code, comments and blank space in C and
  C++ source files
- script for finding missing and packaging crystal icons.
- kdelnk to desktop and zonetab2pot converter
- set of kde-build scripts
- set of scripts that allow more comfortable profiling of KDE apps
- set of scripts to fix licence header/KDE includes directives and
  strip irrelevant tags from .ui files
- KDE man pages generator
- multi-frame PNG to MNG converter

%description scripts-developer -l pl.UTF-8
Ten pakiet zawiera:
- skrypt, który wyciąga łańcuchy z plików .rc aplikacji, np.
  testappgui.rc i zapisuje je do plików pot, z których tworzy się
  tłumaczenia (pliki po)
- skrypt zliczający linijki kodu, komentarzy i znaków białych w
  plikach źródłowych C i C++
- skrypt do wyszukiwania brakujących i pakietowania ikon z motywu
  crystal.
- konwerter plików kdelnk na desktop i zonetab na pot
- zestaw skryptów kde-build
- zestaw skryptów umożliwiających wygodne profilowanie aplikacji KDE
- zestaw skryptów do poprawiania nagłówków informujących o licencji i
  dyrektyw w plikach nagłówkowych KDE oraz usuwania nieistotnych
  znaczników z plików .ui
- generator stron man dla KDE
- konwerter wieloramkowych PNG na MNG

%package scripts-cvs
Summary:	A set of scripts for maintaining KDE from CVS
Summary(pl.UTF-8):	Zestaw skryptów do zarządzania KDE z CVS
Group:		X11/Development/Tools
Requires:	/usr/bin/perl

%description scripts-cvs
A set of scripts for maintaining KDE from CVS.

%description scripts-cvs -l pl.UTF-8
Zestaw skryptów do zarządzania KDE z CVS.

%package scripts-doc
Summary:	A set of scripts for quick access to Qt/KDE documentation
Summary(pl.UTF-8):	Zestaw skryptów szybkiego dostępu do dokumentacji Qt/KDE
Group:		X11/Development/Tools

%description scripts-doc
A set of scripts for quick access to Qt/KDE documentation.

%description scripts-doc -l pl.UTF-8
Zestaw skryptów szybkiego dostępu do dokumentacji Qt/KDE.

%package scripts-kdekillall
Summary:	A script for killing KDE apps started with kdeinit
Summary(pl.UTF-8):	Skrypt do unicestwiania aplikacji KDE uruchomionych przez kdeinit
Group:		X11/Development/Tools

%description scripts-kdekillall
A script for killing KDE apps started with kdeinit.

%description scripts-kdekillall -l pl.UTF-8
Skrypt do unicestwiania aplikacji KDE uruchomionych przez kdeinit.

%package scheck
Summary:	KDE Style - Scheck
Summary(pl.UTF-8):	Motyw KDE - Scheck
Group:		X11/Development/Tools

%description scheck
Development style for searching accelerator and style guide conflicts.

%description scheck -l pl.UTF-8
Motyw KDE przeznaczony do szukania konfliktów w akceleratorach oraz
sprawdzania zgodności z wytycznymi dot. wyglądu graficznego aplikacji
KDE.

%package umbrello
Summary:	UML Modeler
Summary(pl.UTF-8):	Modeler UML
Group:		X11/Development/Tools
Obsoletes:	umbrello

%description umbrello
Umbrello UML Modeller is a UML diagram tool that can support you in
the software development process. Especially during the analysis and
design phases of this process, Umbrello UML Modeller will help you to
get a high quality product. UML can also be used to document your
software designs to help you and your fellow developers.

UML is the diagramming language used to describing such models. You
can represent your ideas in UML using different types of diagrams.
Umbrello UML Modeller 1.2 supports the following types:
- class Diagram
- sequence Diagram
- collaboration Diagram
- use Case Diagram
- state Diagram
- activity Diagram
- component Diagram

%description umbrello -l pl.UTF-8
Modeler UML Umbrello to narzędzie do diagramów UML pomagające w
procesie tworzenia oprogramowania. Szczególnie podczas etapów analizy
i projektowania, modeler UML Umbrello może pomóc w uzyskaniu wysokiej
jakości produktu. UML może być używany do dokumentowania projektu
programu, aby pomóc programiście i jego współpracownikom.

UML to język diagramów używany do opisu takich modeli. Można
przedstawiać idee w UML-u przy użyciu różnych rodzajów diagramów.
Modeler UML Umbrello 1.2 obsługuje następujące rodzaje:
 - diagram klas
 - diagram sekwencji
 - diagram współpracy
 - diagram przypadków użycia
 - diagram stanów
 - diagram aktywności
 - diagram składników.

%package kpartloader
Summary:	UML Modeler
Summary(pl.UTF-8):	Modeler UML
Group:		X11/Development/Tools

%description kpartloader
UML Modeller

%description kpartloader -l pl.UTF-8
Modeler UML

%package strigi-analyzer
Summary:	Strigi Analyzer
Summary(pl.UTF-8):	Strigi Analyzer
Group:		X11/Development/Tools

%description strigi-analyzer
Strigi Analyzer.

%description strigi-analyzer -l pl.UTF-8
Strigi Analyzer.

%package -n kde-kio-svn
Summary:	SVN protocol service
Summary(pl.UTF-8):	Obsługa protokołu SVN
Group:		X11/Libraries
Requires:	kde4-kdelibs >= %{version}

%description -n kde-kio-svn
SVN protocol service.

%description -n kde-kio-svn -l pl.UTF-8
Obsługa protokołu SVN.

%package -n kde-kio-slave
Summary:	kde-kio-slave
Summary(pl.UTF-8):	kde-kio-slave
Group:		X11/Libraries
Requires:	kde4-kdelibs >= %{version}

%description -n kde-kio-slave
kde-kio-slave.

%description -n kde-kio-slave -l pl.UTF-8
kde-kio-slave.


%package kate
Summary:	KDE Advanced Text Editor
Summary(pl.UTF-8):	Zaawansowany edytor tekstu dla KDE
Group:		X11/Applications/Editors

%description kate
KDE advanced text editor featuring among others:
- fast opening/editing of files even the big ones (opens a 50MB file
  in a few seconds)
- powerful syntaxhighlighting engine, extensible via XML files
- Code Folding capabilities for C++, C, PHP and more
- Dynamic Word Wrap - long lines are wrapped at the window border on
  the fly for better overview
- multiple views allows you to view more instances of the same
  document and/or more documents at one time
- support for different encodings globally and at write time
- built in dockable terminal emulation
- sidebars with a list of open documents, a directory viewer with a
  directory chooser, a filter chooser and more
- a plugin interface to allow third party plugins
- a "Filter" command allows you to run selected text through a shell
  command

%description kate -l pl.UTF-8
Kate (KDE advanced text editor) to zaawansowany edytor tekstu KDE o
możliwościach obejmujących m.in.:
- szybkie otwieranie i edycję nawet dużych plików (otwiera plik 50MB w
  parę sekund)
- potężny silnik podświetlania składni, rozszerzalny za pomocą plików
  XML
- możliwość zwijania kodu dla C++, C, PHP i innych języków
- dynamiczne zawijanie wierszy - długie linie są zawijane na granicy
  okna w locie dla lepszej widoczności
- wiele widoków pozwalających oglądać więcej instancji tego samego
  dokumentu i/lub więcej dokumentów w tym samym czasie
- obsługę różnych kodowań globalnie i w czasie zapisu
- wbudowaną emulację dokowalnego terminala
- paski z listą otwartych dokumentów, przeglądarkę katalogów z
  możliwością wybierania katalogu i filtrów
- interfejs wtyczek obsługujący zewnętrzne wtyczki
- polecenie "Filtr" pozwalające przepuszczać zaznaczony tekst przez
  polecenie powłoki

%prep
%setup -q -n %{orgname}-%{version}
#%patch100 -p0
%patch0 -p0

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:release}%{?debug:debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gimpdir}/palettes,%{_appdefsdir}}

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

install ./kdepalettes/KDE_Gimp	$RPM_BUILD_ROOT%{_gimpdir}/palettes
install ./kdepalettes/kde_xpaintrc	$RPM_BUILD_ROOT%{_appdefsdir}/XPaint.kde

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang	cervisia	--with-kde
%find_lang	kapptemplate	--with-kde
%find_lang	kate		--with-kde
%find_lang	kate-plugins	--with-kde
cat kate-plugins.lang >> kate.lang
%find_lang	kcachegrind	--with-kde
%find_lang	kbugbuster	--with-kde
%find_lang	kompare		--with-kde
%find_lang	umbrello	--with-kde
%find_lang	kdesvn-build 	--with-kde
%find_lang	lokalize	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	kompare			-p /sbin/ldconfig
%postun	kompare			-p /sbin/ldconfig

%post	kspy			-p /sbin/ldconfig
%postun	kspy			-p /sbin/ldconfig

%post	kstartperf		-p /sbin/ldconfig
%postun	kstartperf		-p /sbin/ldconfig

#%post	libcvsservice		-p /sbin/ldconfig
#%postun	libcvsservice		-p /sbin/ldconfig

%files cervisia -f cervisia.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cervisia
%attr(755,root,root) %{_bindir}/cvsaskpass
%attr(755,root,root) %{_bindir}/cvsservice
%attr(755,root,root) %{_libdir}/libkdeinit4_cervisia.so
%attr(755,root,root) %{_libdir}/libkdeinit4_cvsservice.so
%attr(755,root,root) %{_libdir}/libkdeinit4_cvsaskpass.so
%attr(755,root,root) %{_libdir}/kde4/*cervisia*.so
%{_datadir}/apps/cervisia*
%{_datadir}/config.kcfg/cervisiapart.kcfg
%{_datadir}/apps/kconf_update/cervisia.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/change_colors.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/cervisia-change_repos_list.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/cervisia-normalize_cvsroot.pl
%{_datadir}/dbus-1/interfaces/*.cervisia.*.xml
%{_datadir}/kde4/services/cvsservice.desktop
%{_datadir}/kde4/services/cervisiapart.desktop
%{_desktopdir}/kde4/cervisia.desktop
%{_iconsdir}/*/*/actions/vcs_*.*
%{_iconsdir}/*/*/*/cervisia.png
%{_mandir}/man1/cervisia.1*


#%files completions-bash
#%defattr(644,root,root,755)
#%{_sysconfdir}/bash_completion.d/*

#%files completions-zsh
#%defattr(644,root,root,755)
#%{_zshfcdir}/*

%files lokalize -f lokalize.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lokalize
%{_desktopdir}/kde4/lokalize.desktop
%{_datadir}/config.kcfg/lokalize.kcfg
%{_datadir}/apps/lokalize
%{_iconsdir}/*/*/actions/msgid2msgstr.png
%{_iconsdir}/*/*/actions/insert_arg.png
%{_iconsdir}/*/*/actions/prevfuzzy.png
%{_iconsdir}/*/*/actions/insert_tag.png
%{_iconsdir}/*/*/actions/approved.png
%{_iconsdir}/*/*/actions/diff.png
%{_iconsdir}/*/*/actions/preverror.png
%{_iconsdir}/*/*/actions/prevfuzzyuntrans.png
%{_iconsdir}/*/*/actions/search2msgstr.png
%{_iconsdir}/*/*/apps/lokalize.png
%{_iconsdir}/*/*/actions/nexterror.png
%{_iconsdir}/*/*/actions/nextfuzzy.png
%{_iconsdir}/*/*/actions/nextfuzzyuntrans.png
%{_iconsdir}/*/*/actions/nextuntranslated.png
%{_iconsdir}/*/*/actions/prevuntranslated.png
%{_iconsdir}/*/*/actions/transsearch.png
%{_iconsdir}/*/*/actions/catalogmanager.png
%{_iconsdir}/*/*/actions/approved.svgz
%{_iconsdir}/*/*/apps/lokalize.svgz

%files kate -f kate.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kate
%attr(755,root,root) %{_libdir}/libkateinterfaces.so.*.*.*
%attr(755,root,root) %{_libdir}/libkateinterfaces.so.?
%attr(755,root,root) %{_libdir}/libkateinterfaces.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kate.so
%attr(755,root,root) %{_libdir}/kde4/kate_kttsd.so
%attr(755,root,root) %{_libdir}/kde4/katepybrowseplugin.so
%attr(755,root,root) %{_libdir}/kde4/katexmlcheckplugin.so
%attr(755,root,root) %{_libdir}/kde4/katebacktracebrowserplugin.so
%attr(755,root,root) %{_libdir}/kde4/katebuildplugin.so
%attr(755,root,root) %{_libdir}/kde4/katectagsplugin.so
%attr(755,root,root) %{_libdir}/kde4/katesnippetsplugin.so
%attr(755,root,root) %{_libdir}/kde4/kateopenheaderplugin.so
%attr(755,root,root) %{_libdir}/kde4/katetextfilterplugin.so
%attr(755,root,root) %{_libdir}/kde4/katefindinfilesplugin.so
%attr(755,root,root) %{_libdir}/kde4/katemailfilesplugin.so
%attr(755,root,root) %{_libdir}/kde4/kateexternaltoolsplugin.so
%attr(755,root,root) %{_libdir}/kde4/katekonsoleplugin.so
%attr(755,root,root) %{_libdir}/kde4/katefiletemplates.so
%attr(755,root,root) %{_libdir}/kde4/katesymbolviewerplugin.so
%attr(755,root,root) %{_libdir}/kde4/katetabbarextensionplugin.so
%attr(755,root,root) %{_libdir}/kde4/katefilebrowserplugin.so
%attr(755,root,root) %{_libdir}/kde4/katequickdocumentswitcherplugin.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_katesession.so
%{_datadir}/apps/kate
%{_datadir}/apps/katepart
%{_datadir}/apps/kconf_update/kate-2.4.upd
%{_datadir}/config/katefiletemplates.knsrc
%{_datadir}/config/katerc
%{_datadir}/kde4/services/kate*.desktop
%{_datadir}/kde4/services/plasma-applet-katesession.desktop
%{_datadir}/kde4/servicetypes/kateplugin.desktop
%{_desktopdir}/kde4/kate.desktop
%dir %{_includedir}/kate
%{_includedir}/kate/*.h
%{_includedir}/kate_export.h
%{_iconsdir}/*/*/apps/kate.*

%files kapptemplate -f kapptemplate.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kapptemplate
%{_datadir}/config.kcfg/kapptemplate.kcfg
%{_desktopdir}/kde4/kapptemplate.desktop
%dir %{_datadir}/apps/kdevappwizard
%{_datadir}/apps/kdevappwizard/templates
%{_iconsdir}/*/*x*/apps/kapptemplate.*

%files kde-resource-kdeaccounts
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kabcformat_kdeaccounts.so
%{_datadir}/apps/kabc/formats/*

%files kde-resource-bugzilla
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcal_bugzilla.so
%{_datadir}/kde4/services/kresources/kcal/bugzilla.desktop

%files kbugbuster -f kbugbuster.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbugbuster
%{_datadir}/apps/kbugbuster
%{_desktopdir}/kde4/kbugbuster.desktop
%{_iconsdir}/hicolor/*/*/kbugbuster.png

%files kcachegrind -f kcachegrind.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcachegrind
%attr(755,root,root) %{_bindir}/hotshot2calltree
%attr(755,root,root) %{_bindir}/op2calltree
%attr(755,root,root) %{_bindir}/pprof2calltree
%attr(755,root,root) %{_bindir}/dprof2calltree
%attr(755,root,root) %{_bindir}/memprof2calltree
%{_datadir}/apps/kcachegrind
%{_desktopdir}/kde4/kcachegrind.desktop
%{_iconsdir}/hicolor/*/apps/kcachegrind.png

%files kmtrace
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/demangle
%attr(755,root,root) %{_bindir}/kminspector
%attr(755,root,root) %{_bindir}/kmmatch
%attr(755,root,root) %{_bindir}/kmtrace
%attr(755,root,root) %{_libdir}/libktrace*.so*
%{_datadir}/apps/kmtrace
%{_includedir}/ktrace.h

%files kompare -f kompare.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kompare
%attr(755,root,root) %{_libdir}/libkompareinterface.so.*.*.*
%attr(755,root,root) %{_libdir}/libkompareinterface.so
%attr(755,root,root) %{_libdir}/libkomparedialogpages.so
%attr(755,root,root) %{_libdir}/libkomparediff2.so
%attr(755,root,root) %{_libdir}/kde4/libkomparenavtreepart.so
%attr(755,root,root) %{_libdir}/kde4/libkomparepart.so
%attr(755,root,root) %{_libdir}/libkomparediff2.so.*.*.*
%attr(755,root,root) %{_libdir}/libkompareinterface.so.?
%attr(755,root,root) %{_libdir}/libkomparedialogpages.so.*.*.*
%attr(755,root,root) %{_libdir}/libkomparedialogpages.so.?
%attr(755,root,root) %{_libdir}/libkomparediff2.so.?
%{_datadir}/apps/kompare*
%{_datadir}/kde4/services/kompare*.desktop
%{_datadir}/kde4/servicetypes/kompare*.desktop
%{_desktopdir}/kde4/kompare.desktop
%{_iconsdir}/*/*/*/kompare.*

%files kprofilemethod
%defattr(644,root,root,755)
%{_includedir}/kprofilemethod.h

#%files kspy
#%defattr(644,root,root,755)
#%{_libdir}/libkspy.so
#%attr(755,root,root) %{_libdir}/libkspy.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkspy.so.1
#%{_includedir}/kspy.h
#%{_mandir}/man1/testkspy.1*

%files kstartperf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kstartperf
%{_libdir}/libkstartperf.so
%attr(755,root,root) %{_libdir}/libkstartperf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkstartperf.so.?

%files kuiviewer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kuiviewer
%attr(755,root,root) %{_libdir}/kde4/libkuiviewerpart.so
%attr(755,root,root) %{_libdir}/kde4/quithumbnail.so
%dir %{_datadir}/apps/kuiviewer
%{_datadir}/apps/kuiviewer/kuiviewerui.rc
%dir %{_datadir}/apps/kuiviewerpart
%{_datadir}/apps/kuiviewerpart/kuiviewer_part.rc
%{_datadir}/kde4/services/designerthumbnail.desktop
%{_datadir}/kde4/services/kuiviewer_part.desktop
%{_desktopdir}/kde4/kuiviewer.desktop
%{_iconsdir}/*/*/apps/kuiviewer.png

#%files kunittest
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kunit*
#%attr(755,root,root) %{_libdir}/libkunittestgui.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkunittestgui.so.0
#%attr(755,root,root) %{_libdir}/libkunittestgui.so
#%{_includedir}/kunittest

#%files libcvsservice
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libcvsservice.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libcvsservice.so.0
#%attr(755,root,root) %{_libdir}/libkdeinit_cvsservice.so
#%attr(755,root,root) %{_libdir}/libkdeinit_cvsaskpass.so
#%attr(755,root,root) %{_libdir}/kde4/cvs*.so

#%files libcvsservice-devel
#%defattr(644,root,root,755)
#%{_includedir}/cvsjob_stub.h
#%{_includedir}/cvsservice_stub.h
#%{_includedir}/repository_stub.h
#%attr(755,root,root) %{_libdir}/libcvsservice.so

%files palette-gimp
%defattr(644,root,root,755)
%{_gimpdir}/palettes

%files palette-xpaint
%defattr(644,root,root,755)
%{_appdefsdir}/*

%files po2xml
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/po2xml
%attr(755,root,root) %{_bindir}/split2po
%attr(755,root,root) %{_bindir}/swappo
%attr(755,root,root) %{_bindir}/xml2pot
%attr(755,root,root) %{_libdir}/libantlr.so.*.*.*
%attr(755,root,root) %{_libdir}/libantlr.so.?
%attr(755,root,root) %{_libdir}/libantlr.so

#%files scheck
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/plugins/styles/scheck.so
#%{_datadir}/apps/kstyle/themes/scheck.themerc

%files scripts-developer -f kdesvn-build.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/adddebug
%attr(755,root,root) %{_bindir}/build-progress.sh
%attr(755,root,root) %{_bindir}/create*
%attr(755,root,root) %{_bindir}/cheatmake
%attr(755,root,root) %{_bindir}/extend*
%attr(755,root,root) %{_bindir}/extractattr
%attr(755,root,root) %{_bindir}/fixkdeincludes
%attr(755,root,root) %{_bindir}/fixuifiles
%attr(755,root,root) %{_bindir}/includemocs
%attr(755,root,root) %{_bindir}/kdemangen.pl
%attr(755,root,root) %{_bindir}/krazy-licensecheck
%attr(755,root,root) %{_bindir}/makeobj
%attr(755,root,root) %{_bindir}/dprof2calltree
%attr(755,root,root) %{_bindir}/hotshot2calltree
%attr(755,root,root) %{_bindir}/memprof2calltree
%attr(755,root,root) %{_bindir}/op2calltree
%attr(755,root,root) %{_bindir}/png2mng.pl
%attr(755,root,root) %{_bindir}/pprof2calltree
%attr(755,root,root) %{_bindir}/cxxmetric
%attr(755,root,root) %{_bindir}/extractrc
%attr(755,root,root) %{_bindir}/findmissingcrystal
%attr(755,root,root) %{_bindir}/kdelnk2desktop.py
%attr(755,root,root) %{_bindir}/package_crystalsvg
%attr(755,root,root) %{_bindir}/zonetab2pot.py
%attr(755,root,root) %{_bindir}/fix-include.sh
%attr(755,root,root) %{_bindir}/kde_generate_export_header
%attr(755,root,root) %{_bindir}/optimizegraphics
%attr(755,root,root) %{_bindir}/wcgrep
%{_datadir}/apps/katepart/syntax/kdesvn-buildrc.xml
%{_desktopdir}/kde4/kdesvn-build.desktop

%files scripts-cvs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cvs*
%exclude %{_bindir}/cvsaskpass
%exclude %{_bindir}/cvsservice
%attr(755,root,root) %{_bindir}/noncvslist
%attr(755,root,root) %{_bindir}/pruneemptydirs

%files scripts-doc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdedoc
%attr(755,root,root) %{_bindir}/qtdoc

%files scripts-kdekillall
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdekillall

%files umbrello -f umbrello.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/umbrello
%{_datadir}/apps/umbrello
%{_desktopdir}/kde4/umbrello.desktop
%{_iconsdir}/*/*x*/*/umbrello*.*

%files kpartloader
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpartloader
%dir %{_datadir}/apps/kpartloader
%{_datadir}/apps/kpartloader/kpartloaderui.rc

%files strigi-analyzer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/strigi/strigila_diff.so
%attr(755,root,root) %{_libdir}/strigi/strigita_ts.so
%attr(755,root,root) %{_libdir}/strigi/strigila_po.so
%{_datadir}/strigi/fieldproperties/strigi_translation.fieldproperties

%files -n kde-kio-svn
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*svn*
%attr(755,root,root) %{_libdir}/kde4/kio_svn.so
%attr(755,root,root) %{_libdir}/kde4/kded_ksvnd.so
%{_datadir}/kde4/services/kded/*svn*.desktop
%{_datadir}/kde4/services/ServiceMenus/subversion*.desktop
%{_datadir}/kde4/services/svn*.protocol
%{_datadir}/dbus-1/interfaces/org.kde.ksvnd.xml
%{_iconsdir}/*/*/*/*svn*.*

%files -n kde-kio-slave
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kio_perldoc.so
%dir %{_datadir}/apps/kio_perldoc
#%{_datadir}/apps/kio_perldoc/kio_perldoc.css
%{_datadir}/apps/kio_perldoc/pod2html.pl
%{_datadir}/kde4/services/perldoc.protocol

Summary:	DuMP3 - duplicate & similar file finder
Summary(pl):	DuMP3 - program do znajdywania powt�rzonych i podobnych plik�w
Name:		dump3
Version:	0.2.9
Release:	0.1
License:	GPL
Group:		Applications/File
Source0:	http://dl.sourceforge.net/dump3/%{name}_morpheus_%{version}_src.zip
# Source0-md5:	97b3fbad6597ea536213db57e8c0eeb0
URL:		http://dump3.sourceforge.net/en/index.html
BuildRequires:	ant
BuildRequires:	jaxp_parser_impl
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.294
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DuMP3 can find files that are not exact duplicates:
- Binary files are compared by SHA1 hash (configurable to any MD hash)
- Text files that were changed by addition or deletion (2 fingerprint
  algorithms available)
- Pictures in different formats, sizes and/or rotations (BMP, GIF,
  JPEG, JPEG2000, PNG, PNM, RAW, TIFF)
- Audio files that were recorded at different bit rates or saved in
  different formats (AU, AIF, WAV, MP3, OGG)
- plugin fingerprint classes can be written for any file where inexact
  matching is needed (fonts, videos, etc)

%description -l pl
DuMP3 potrafi znale�� pliki nie b�d�ce dok�adnymi duplikatami:
- binarne pliki s� por�wnywane za pomoc� skr�tu SHA1 (konfigurowalne
  do dowolnego skr�tu MD)
- pliki tekstowe zmienione przez dodanie lub usuni�cie (dost�pne dwa
  algorytmy "odcisk�w palca")
- obrazki w r�nych formatach, rozmiarach i/lub orientacjach (BMP,
  GIF, JPEG, JPEG2000, PNG, PNM, RAW, TIFF)
- pliki d�wi�kowe zapisane z r�n� pr�dko�ci� strumienia lub w r�nych
  formatach (AU, AIF, WAV, MP3, OGG)
- mo�na dopisywa� wtyczki "odcisk�w palc�w" dla dowolnych format�w
  plik�w wymagaj�cych niedok�adnego por�wnywania (font�w, film�w itp.)

%prep
%setup -q -c

%build
%ant build

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

%define		_snap	20031202
Summary:	VideoLAN Server
Summary(pl):	Serwer VideoLAN
Name:		vls
Version:	0.5.3
Release:	0.%{_snap}.3
License:	GPL
Group:		Applications/Multimedia
#Source0:	http://www.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}-%{_snap}.tar.gz
# Source0-md5:	363971bcfab1d32a63794590eed1aa5c
URL:		http://www.videolan.org/
BuildRequires:	ffmpeg-devel
BuildRequires:	libdvb-devel
BuildRequires:	libdvbpsi-devel
BuildRequires:	libdvdread-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The VideoLAN project targets multimedia streaming of MPEG-1, MPEG-2,
MPEG-4 and DivX files, DVDs, digital satellite channels, digital
terrestial television channels and live videos on a high-bandwidth
IPv4 or IPv6 network in unicast or multicast under many OSes.

%description -l pl
Projekt VideoLAN zajmuje siê multimedialnymi strumieniami MPEG-1,
MPEG-2, MPEG-4 oraz plikami DivX, danymi DVD, cyfrowymi kana³ami
satelitarnymi, cyfrowymi kana³ami telewizji naziemnej oraz obrazem
trasmitowanym na ¿ywo po wysokoprzepustowej sieci IPv4 lub IPv6
w trybie unicast lub multicast pod kontrol± wielu systemów
operacyjnych.

%package dvd
Summary:	DVD input for VideoLAN Server
Summary(pl):	Wej¶cie DVD dla serwera VideoLAN
Group:		Application/Multimedia
Requires:	%{name} = %{version}-%{release}

%description dvd
This package includes the DVD input plugin for vls, the VideoLAN
Server. With this plugin vls is able to read MPEG data from a DVD and
send the stream to the network, together with all subtitles and audio
tracks.

%description dvd -l pl
Ten pakiet zawiera wtyczkê wej¶ciow± DVD dla vls - serwera VideoLAN.
Przy pomocy tej wtyczki vls mo¿e odczytywaæ dane MPEG z DVD i wysy³aæ
strumieñ w sieæ wraz z wszystkimi napisami i ¶cie¿kami d¼wiêkowymi.

%package dvb
Summary:	DVB input for VideoLAN Server
Summary(pl):	Wej¶cie DVB dla serwera VideoLAN
Group:		Application/Multimedia
Requires:	%{name} = %{version}-%{release}

%description dvb
This package includes the DVB input plugin for the VideoLAN Server. It
allows reception of digital unencrypted satellite channels and digital
unencrypted terrestial television channels from a DVB device using the
DVB drivers from linuxtv.org.

%description dvb -l pl
Ten pakiet zawiera wtyczkê wej¶ciow± DVB dla serwera VideoLAN. Pozwala
ona odbieraæ cyfrowe nieszyfrowane kana³y satelitarne i cyfrowe
nieszyfrowane kana³y telewizji naziemnej z urz±dzenia DVB przy u¿yciu
sterowników DVB z linuxtv.org.

%prep
%setup -q

%build
./bootstrap #CVS snap specyfic
%configure \
	--enable-dvb \
	--enable-v4l \
	--with-libdvb=%{_libdir} \
	--with-ffmpeg=%{_includedir}/ffmpeg #this don't work
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# help rpm find dependencies
chmod 755 $RPM_BUILD_ROOT%{_libdir}/videolan/%{name}/*.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO doc/vls-guide.sgml
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/videolan
%dir %{_libdir}/videolan/%{name}
%dir %{_sysconfdir}/videolan
%dir %{_sysconfdir}/videolan/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/videolan/%{name}/%{name}.cfg

%files dvd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/videolan/%{name}/dvdreader.so

%files dvb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/videolan/%{name}/dvbinput.so
%attr(755,root,root) %{_libdir}/videolan/%{name}/dvbreader.so

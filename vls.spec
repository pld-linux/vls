Summary:	VideoLAN Server
Summary(pl):	Serwer VideoLAN
Name:		vls
Version:	0.5.3
Release:	0.3
License:	GPL
Group:		Applications/Multimedia
Source0:	http://www.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	63fb39e7312fdd87f27e2e4c99593143
URL:		http://www.videolan.org/
BuildRequires:	libdvbpsi-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The VideoLAN project targets multimedia streaming of MPEG-1, MPEG-2,
MPEG-4 and DivX files, DVDs, digital satellite channels, digital
terrestial television channels and live videos on a high-bandwidth
IPv4 or IPv6 network in unicast or multicast under many OSes.

%description -l pl
Projekt VideoLAN zajmuje si� multimedialnymi strumieniami MPEG-1,
MPEG-2, MPEG-4 oraz plikami DivX, danymi DVD, cyfrowymi kana�ami
satelitarnymi, cyfrowymi kana�ami telewizji naziemnej oraz obrazem
trasmitowanym na �ywo po wysokoprzepustowej sieci IPv4 lub IPv6
w trybie unicast lub multicast pod kontrol� wielu system�w
operacyjnych.

%package -n %{name}-dvd
Summary:        DVD input for VideoLAN Server
Group:          Application/Multimedia
Requires:       libdvdread
Requires:       %{name} = %{version}
Buildrequires:  libdvdread-devel

%description -n %{name}-dvd
The %{name}-dvd package includes the DVD input plugin for vls, the VideoLAN
Server.
With this plugin vls is able to read MPEG data from a DVD and send the
stream to the network, together with all subtitles and audio tracks.

%package -n %{name}-dvb
Summary:        DVB input for VideoLAN Server
Group:          Application/Multimedia
Requires:       %{name} = %{version}
Buildrequires: libdvb-devel

%description -n %{name}-dvb
The %{name}-dvb package includes the DVB input plugin for the VideoLAN
Server.
It allows reception of digital unencrypted satellite channels and
digital unencrypted terrestial television channels from a DVB device
using the DVB drivers from linuxtv.org.


%prep
%setup -q

%build
%configure --enable-dvb \
	--enable-v4l \
	--with-libdvb=%{_libdir}
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

%files -n %{name}-dvd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/videolan/%{name}/dvdreader.so

%files -n %{name}-dvb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/videolan//%{name}/dvbinput.so
%attr(755,root,root) %{_libdir}/videolan//%{name}/dvbreader.so

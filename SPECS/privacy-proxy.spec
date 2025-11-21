Name:           privacy-tor-proxy
Version:        1.0
Release:        1%{?dist}
Summary:        Overwrite configs for Tor, Privoxy, and HAProxy

License:        Proprietary
Source0:        torrc.cfg
Source1:        privoxy.cfg
Source2:        haproxy.cfg

Requires:       tor
Requires:       privoxy
Requires:       haproxy
Requires(post): /bin/systemctl

%description
This package installs custom configuration files that overwrite the default
configs of tor, privoxy, and haproxy. It assumes these services are managed
by systemd.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/privacy-proxy/configs
install -m 644 %{SOURCE0} %{buildroot}/usr/share/privacy-proxy/configs/torrc.cfg
install -m 644 %{SOURCE1} %{buildroot}/usr/share/privacy-proxy/configs/privoxy.cfg
install -m 644 %{SOURCE2} %{buildroot}/usr/share/privacy-proxy/configs/haproxy.cfg

%post
/bin/cp -f /usr/share/privacy-proxy/configs/torrc.cfg /etc/tor/torrc
/bin/cp -f /usr/share/privacy-proxy/configs/privoxy.cfg /etc/privoxy/config
/bin/cp -f /usr/share/privacy-proxy/configs/haproxy.cfg /etc/haproxy/haproxy.cfg
systemctl reload tor privoxy haproxy >/dev/null 2>&1 || :
systemctl start tor
systemctl start privoxy
systemctl start haproxy

%files
/usr/share/privacy-proxy/configs/torrc.cfg
/usr/share/privacy-proxy/configs/privoxy.cfg
/usr/share/privacy-proxy/configs/haproxy.cfg

%changelog
* Fri Nov 21 2025 Your Name <you@example.com> - 1.0-1
- Initial config overwrite package

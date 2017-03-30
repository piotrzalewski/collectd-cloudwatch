Name: 		collectd-cloudwatch		
Version: 	0.1
Release:	1
Summary:	Plugin for collectd to put metrics in AWS Cloudwatch	
Group:		System/Base
License:	Other	
URL:		https://github.com/piotrzalewski/collectd-cloudwatch
Source0:	https://github.com/piotrzalewski/collectd-cloudwatch
BuildArch:      noarch
Requires:	collectd,python-pip,python-setuptools
Packager:	Piotr Zalewski

%description
Plugin for collect to put metrics in AWS Cloudwatch

%prep
mkdir -p  $RPM_SOURCE_DIR/collectd-cloudwatch

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p  $RPM_BUILD_ROOT/opt/collectd-plugins/cloudwatch
mkdir -p  ${RPM_BUILD_ROOT}/opt/collectd-plugins/cloudwatch/config/
mkdir -p ${RPM_BUILD_ROOT}/etc/collectd.d/
cp -r $RPM_SOURCE_DIR/../../src/cloudwatch  ${RPM_BUILD_ROOT}/opt/collectd-plugins
install $RPM_SOURCE_DIR/../../src/cloudwatch_writer.py  ${RPM_BUILD_ROOT}/opt/collectd-plugins
install $RPM_SOURCE_DIR/../../src/__init__.py  ${RPM_BUILD_ROOT}/opt/collectd-plugins
install $RPM_SOURCE_DIR/../../resources/collectd-cloudwatch.conf ${RPM_BUILD_ROOT}/etc/collectd.d/
install $RPM_SOURCE_DIR/collectd-cloudwatch/plugin.conf   ${RPM_BUILD_ROOT}/opt/collectd-plugins/cloudwatch/config/plugin.conf



%post
pip-python  install --quiet --upgrade --force-reinstall requests

%clean
rm -rf ${RPM_BUILD_ROOT}


%files
/opt/collectd-plugins/
/etc/collectd.d/collectd-cloudwatch.conf

%changelog


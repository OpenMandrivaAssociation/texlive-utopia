# revision 15878
# category Package
# catalog-ctan /fonts/utopia
# catalog-date 2007-10-04 10:35:17 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-utopia
Version:	20180303
Release:	1
Summary:	Adobe Utopia fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/utopia
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/utopia.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/utopia.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Adobe Standard Encoding set (upright and italic shapes,
medium and bold weights) of the Utopia font family, which Adobe
donated to the X Consortium. Macro support, and maths fonts
that match the Utopia family, are provided by the Fourier and
the Mathdesign Utopia font packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/adobe/utopia/putb8a.afm
%{_texmfdistdir}/fonts/afm/adobe/utopia/putbi8a.afm
%{_texmfdistdir}/fonts/afm/adobe/utopia/putr8a.afm
%{_texmfdistdir}/fonts/afm/adobe/utopia/putri8a.afm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putb7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putb8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putb8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putb8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putbc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putbc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putbi7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putbi8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putbi8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putbi8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putbo7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putbo8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putbo8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putbo8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putr7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putr8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putr8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putr8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putrc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putrc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putri7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putri8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putri8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putri8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putro7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putro8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putro8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/utopia/putro8t.tfm
%{_texmfdistdir}/fonts/type1/adobe/utopia/putb8a.pfb
%{_texmfdistdir}/fonts/type1/adobe/utopia/putbi8a.pfb
%{_texmfdistdir}/fonts/type1/adobe/utopia/putr8a.pfb
%{_texmfdistdir}/fonts/type1/adobe/utopia/putri8a.pfb
%{_texmfdistdir}/fonts/vf/adobe/utopia/putb7t.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putb8c.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putb8t.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putbc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putbc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putbi7t.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putbi8c.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putbi8t.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putbo7t.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putbo8c.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putbo8t.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putr7t.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putr8c.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putr8t.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putrc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putrc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putri7t.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putri8c.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putri8t.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putro7t.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putro8c.vf
%{_texmfdistdir}/fonts/vf/adobe/utopia/putro8t.vf
%doc %{_texmfdistdir}/doc/fonts/utopia/LICENSE-utopia.txt
%doc %{_texmfdistdir}/doc/fonts/utopia/README-utopia.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20071004-2
+ Revision: 757333
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20071004-1
+ Revision: 719866
- texlive-utopia
- texlive-utopia
- texlive-utopia


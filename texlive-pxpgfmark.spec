%global tl_name pxpgfmark
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	e-pTeX driver for PGF inter-picture connections
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/pxpgfmark
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxpgfmark.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxpgfmark.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The distributed drivers do not support the PGF feature of "inter-picture
connections" under e-pTeX and dvipdfmx. The package uses existing
features of dvipdfmx to fix this problem


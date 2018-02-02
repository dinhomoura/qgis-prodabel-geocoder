pushd %~dp0

SET OSGEO4W_ROOT=C:\OSGeo4W64
CALL %OSGEO4W_ROOT%\bin\o4w_env.bat

pyuic4 -o prodabel_geocoder_dialog_base.py prodabel_geocoder_dialog_base.ui

popd
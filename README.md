# CPAL/COLR-Juggler

CPAL/COLR Juggler (de: *COLR/CPAL-Jongleur,* fr: *Jongleur COLR/CPAL*) randomly rotates color layers between palette colors

For export it makes most sense to copy and paste this prefilter into an instance in *Font Info > Exports* (Cmd-I, Cmd-3):

```
{
customParameters = (
{
name = PreFilter;
value = COLRCPALJuggler;
}
);
}
```

### License

Copyright 2023 Rainer Erich Scheichelbauer (@mekkablue).
Based on sample code by Georg Seifert (@schriftgestalt) and Jan Gerner (@yanone).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.

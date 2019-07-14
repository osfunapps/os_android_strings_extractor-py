Introduction
------------
This project's aim is to help with the translation of an Android app.  
It will extract the strings.xml file of an app to a nice readable xlsx file, which can be sent to translators to work on.  

If, after the translators will finish translating the file, you also interested in converting the translated file back to a strings.xml file,
use the complementary library ([os_android_strings_importer-py](https://github.com/osfunapps/os_android_strings_importer-py)) 


## Installation
Install via pip:

    pip install os_android_strings_extractor

## Usage       
    
Say you have this *strings.xml* file:
    
    <resources>
        <string name="app_name">Memorizer</string>
        <string name="capital">Capital</string>
        <string name="country">Country</string>
        <string name="add_tab">Add List</string>
        <string name="action_settings">Settings</string>
        <string name="settings">Lists Settings</string>
        <string name="save">Save</string>
        <string name="delete">DELETE</string>
        <string name="entries">%1$s Entries</string>
        <string name="entry">%1$s Entry</string>
        <string name="from_definition_hint">Like: Date In History </string>
        <string name="to_definition_hint">To: Event</string>
        <string name="from_translation_hint">Like: Spanish</string>
        <string name="to_translation_hint">To: Hebrew</string>
        <string name="go">Go</string>
        <string name="entries_count">total entries: %1$s</string>
        <string name="entries_hard_count">hard entries: %1$s</string>
        <string name="tabs_list_title" translatable="false">Lists</string>
    </resources>
    
Convert it to a readable excel file:

    import os_android_strings_extractor.StringsExtractor as se
    
    se.run('/path/to/android/project',
           '/output/path',
           src_language='English',
           output_languages_arr=['French', 'German', 'Hindi'])
  
And you will get the output:

![Alt text](os_android_strings_extractor/example_img.png?raw=true "Title")
(notice the worksheets at the bottom -> 'French', 'German', 'Hindi')

    
## Links
[os_android_strings_importer-py](https://github.com/osfunapps/os_android_strings_importer-py) -> Will import an xlsx file (made by os_android_strings_extractor) and convert it to an Android strings.xml file, after translation.


## Licence
MIT
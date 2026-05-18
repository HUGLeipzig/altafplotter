<<<<<<< Updated upstream

# featrue toggle for public version
# if true:
#   Varvis requests are deactivated and only vcf uploads are possible
#   Help-Page and bug reports are redirected to github
toggle_public_version = True

# streamlit page config
if toggle_public_version:
    main_page_config = {
        "page_title" :          "altAF-plotter",
        "page_icon" :           "🦔",
        "page_layout" :         "wide",
        "page_sidebar_state" :  "auto",
        "page_menu_items" : {
            "Get help":     "https://github.com/HUGLeipzig/altafplotter/blob/main/user_guideline/user_guideline.md",
            "Report a Bug": "https://github.com/HUGLeipzig/altafplotter/issues",
            "About" :       """
                [AltAFPlotter-preprint](https://www.biorxiv.org/content/10.1101/2023.08.08.546838v1)\\
                [AltAFPlotter GitHub](https://github.com/HUGLeipzig/altafplotter)\\
                [UPD-Cohort](https://link.springer.com/article/10.1007/s00439-024-02687-w)


                This App is hosted at the [Computing Center of the University Leipzig.](https://www.urz.uni-leipzig.de/en)

                We use:
                - [Streamlit](https://streamlit.io/)
                - [bcftools](https://pubmed.ncbi.nlm.nih.gov/33590861/)
                - [bcftools ROH](https://pubmed.ncbi.nlm.nih.gov/28205675/)
                
                The Institute for Human Genetics (University Medical Center Leipzig) makes no representation about the suitability or accuracy of this software or data for any purpose, and makes no warranties, including fitness for a particular purpose or that the use of this software will not infringe any third party patents, copyrights, trademarks or other rights.\\
                Responsible for this project:
                Maximilian Radtke (maximilian.radtke@medizin.uni-leipzig.de)

                Address:\\
                Philipp-Rosenthal-Str. 55\\
                04103 Leipzig\\
                GERMANY\\
                Phone: +49 341 97 23800
            """
        }
    }

else:
    main_page_config = {
        "page_title" :          "altAF-plotter",
        "page_icon" :           "🦔",
        "page_layout" :         "wide",
        "page_sidebar_state" :  "auto",
        "page_menu_items" : {
            "Get help":     "https://wiki.hugapps.medizin.uni-leipzig.de/xwiki/bin/view/How%20to/altAFplotter-Installation",
            "Report a Bug": "mailto:hug-ito@medizin.uni-leipzig.de",
            "About" :       None
        }
    }

# domain setting for altair
=======
import os
# feature toggle for varvis and gepado
toggle_varvis = False
toggle_gepado = False
toggle_delete_vcfs = True

url_param = "querystring"

DEV = os.environ.get("LOCAL_DEV", "True").lower() in ('true')

# GDS-API
gds_api_base_url = os.environ.get("API_BASE_URL", "")

analysis_id_endpoint = "analysis/{analysis_guid}/analysis_id_from_guid"
person_id_from_analysis_id_endpoint = "analysis/{analysis_id}/person_id_from_analysis_id"
family_id_endpoint = "person/{person_id}/family_id"
family_members_endpoint = "/family/{family_id}/family_members"
person_status_endpoint = "/person/{person_id}/status"

# streamlit page config
main_page_config = {
    "page_title" :          "altAF-plotter",
    "page_icon" :           "🦔",
    "page_layout" :         "wide",
    "page_sidebar_state" :  "auto",
    "page_menu_items" : {
        "Get help":     "https://github.com/maxmilianr/altafplotter_public/blob/main/user_guideline/user_guideline.md",
        "Report a Bug": "https://github.com/maxmilianr/altafplotter_public/issues",
        "About" :       """
            publication link, coming soon
            https://github.com/maxmilianr/altafplotter_public
            
            [Narasimhan V, Danecek P, Scally A, Xue Y, Tyler-Smith C, and Durbin R. BCFtools/RoH: a hidden Markov model approach for detecting autozygosity from next-generation sequencing data. Bioinformatics (2016) 32(11) 1749-51](https://pubmed.ncbi.nlm.nih.gov/28205675/)
            
            [Danecek P, Bonfield JK, et al. Twelve years of SAMtools and BCFtools. Gigascience (2021) 10(2):giab008](https://pubmed.ncbi.nlm.nih.gov/33590861/)
            
            The Institute for Human Genetics (University Medical Center Leipzig) makes no representation about the suitability or accuracy of this software or data for any purpose, and makes no warranties, including fitness for a particular purpose or that the use of this software will not infringe any third party patents, copyrights, trademarks or other rights.
            Responsible for this project:
            Maximilian Radtke (maximilian.radtke@medizin.uni-leipzig.de)
            Address:
            Sekretariat\n
            Philipp-Rosenthal-Str. 55\n
            04103 Leipzig\n
            GERMANY\n
            Telefon: 0341 - 97 23800
        """
    }
}

>>>>>>> Stashed changes

dict_domain = {
    "single" : ["unknown"],
    "trio" : ['biparental', 'de novo', 'maternal', 'paternal', 'unknown'],
    "duo_mat" : ['unknown', 'not maternal', 'maternal'],
    "duo_pat" : ['unknown', 'not paternal', 'paternal']
}
dict_range = {
    "single" : ["blue"],
    "trio" : ['blue', 'orange', 'red', 'green', 'grey'],
    "duo_mat" : ['grey', 'orange', 'red'],
    "duo_pat" : ['grey', 'orange', 'green']
    
}

#inheritance dicts
inheritance_dict_trio = {
                "001"   :   "unknown",
                "010"   :   "unknown",
                "011"   :   "unknown",
                "100"   :   "de novo",
                "101"   :   "paternal",
                "110"   :   "maternal",
                "111"   :   "biparental",
            }
inheritance_dict_duo_mother = {
                "00"   :   "unknown",
                "01"   :   "unknown",
                "10"   :   "not maternal",
                "11"   :   "maternal",
            }
inheritance_dict_duo_father = {
                "00"   :   "unknown",
                "01"   :   "unknown",
                "10"   :   "not paternal",
                "11"   :   "paternal",
            }


# flagging cutoffs:
roh_high_cutoff = 0.7
roh_high_mixed_start = 0.2
roh_high_mixed_end = 0.7

inh_ratio_high_trio_cutoff = 2
inh_ratio_high_duo_cutoff = 5
<<<<<<< Updated upstream
inh_ratio_low_cutoff = 0.5
=======
>>>>>>> Stashed changes

consanguin_min_chr_count = 3
consanguin_roh_cutoff = 0.1

min_snvs_per_chr = 200

# flags
roh_high_tag = "roh_high"
roh_high_mixed_tag = "roh_high_mixed"
inh_ratio_high_tag = "inh_ratio_high"
consanguin_tag = "likely_consanguineous"
not_consanguin_tag = "unlikely_consanguineous"
snv_per_chr_warning = "insufficient_snvs"

<<<<<<< Updated upstream
consanguinity_warning = "Consanguinity likely, handle potential UPD flags with extra care.\n\n"
no_consanguinity = "Consanguinity unlikely.\n\n"

# general
public_tabs = ["vcf Upload", "Demo"]
hug_tabs = ["Varvis", "vcf Upload", "Demo"]

assemply_options = ["hg19", "hg38"]

upd_region_file = "data/upd_regions/upd_regions.json"

temp_file_prefix = "altafplotter_temp_file_"
temp_folder = "/tmp/"

# demo vcfs
demo_vcf_file = "data/demo_files/vcfs/HG001_GRCh38_1_22_v4.2.1_exome.vcf.gz"
demo_altaf = "data/demo_files/csvs/demo_altaf.csv"
demo_origin = "data/demo_files/csvs/demo_origin.csv"
demo_roh = "data/demo_files/csvs/demo_roh.csv"
=======
consanguinity_warning = "Consanguinity likely, handle potential UPD flags with extra care."
no_consanguinity = "Consanguinity unlikely"

demo_altaf = "settings/demo_files/demo_altaf.csv"
demo_origin = "settings/demo_files/demo_origin.csv"
demo_roh = "settings/demo_files/demo_roh.csv"

public_tabs = ["vcf Upload", "Demo"]
hug_tabs = ["Varvis", "vcf Upload", "Demo"]

unwanted_enrichment_kits = [
    "MT Chromosom 100bp regions",
    "Nimagen HEST v2"
]
>>>>>>> Stashed changes

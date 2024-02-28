import ResearchOS as ros

from subsets import static_OA

ss_all_trials_oa = ros.Subset(id = "SS1")
ss_all_trials_ya = ros.Subset(id = "SS2")
ss_static_oa = ros.Subset(id = "SS3")
ss_static_oa.conditions = static_OA

ds = ros.Dataset(id = "DS1")

# 1. Load calibration results
folder_vr = ros.Variable(id = "VR39", name = "folderName", level = ros.Trial)
folder_vr.hard_coded_value = ds.dataset_path
seg_marker_names = ros.Variable(id = "VR40", name = "segMarkerNames", level = ros.Trial)
mocap_data = ros.Variable(id = "VR33")

calib_results = ros.Variable(id = "VR43", name = "calibResults", level = ros.Trial) 
mocap_data_out = ros.Variable(id = "VR44", name = "mocapData", level = ros.Trial)
seg_marker_names_out = ros.Variable(id = "VR45", name = "segMarkerNames_calib", level = ros.Trial)

loadcalib = ros.Process(id = "PR3", name = "loadcalib")
loadcalib.level = ros.Trial
loadcalib.is_matlab = True
loadcalib.set_input_vrs(folderName = folder_vr, segMarkerNames = seg_marker_names, mocapData = mocap_data)
loadcalib.set_output_vrs(calibResults = calib_results, mocapData = mocap_data_out, segMarkerNames = seg_marker_names_out)
loadcalib.subset_id = ss_static_oa.id
loadcalib.mfolder = "C:\\Users\\Mitchell\\Desktop\\Matlab Code\\GitRepos\\PGUI_CommonPath\\Code\\Process_Functions_Copy_For_Python"
loadcalib.mfunc_name = "LoadCalibResults"
loadcalib.run()



# 2. Compute subject height.

# 3. Get the dynamic calibration trial names.

# 4. Compute the subject's mass from FP data.

# 5. Merge the subject's mass from FP and logsheet data.

# 6. Compute the subject's segment parameters per Dumas 2007.

# 7. Compute the static trial ground contact heights.

# 8. Create the tripods

# 9. Define the best marker names per segment.

# 10. Compute the static hip joint center positions.

# 11. Compute the static calibration.

# 12. Put the marker positions into the dynamic trials' feet & pelvis segments.

# 13. Compute the anatomic axes.
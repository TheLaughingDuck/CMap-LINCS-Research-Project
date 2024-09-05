from cmapPy.pandasGEXpress.parse import parse

gctx_file = parse("../level5_beta_trt_misc_n8283x12328.gctx", col_meta_only=True)
gctx_file[0:5]

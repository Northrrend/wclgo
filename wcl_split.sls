e_csv(
    "content",
    "x, u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11, u12, u13, u14, u15, u16, u17, u18, u19, u20, u21, u22, u23, u24, u25, u26, u27, u28, u29, u30, u31",
    restrict=False,
)
e_csv(
    "x", "date, time, type", sep=" ",
)
e_drop_fields("content", "x", regex=False)
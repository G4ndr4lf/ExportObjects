from get_objects import get_objects


fields = {
    "whitelist": ["^name$", "^url-list$", "^application-signature$", "^additional-categories$", "^description$", r"^primary-category$", r"^urls-defined-as-regular-expression$", "^tags$", "^color$", "^comments$"],
    "blacklist": [],
    "translate": [
        # (#1, [(#2, #3)]) -> if field matches with regex #1 then in that field, replace regex #2 with regex #3
    ]
}

if __name__ == "__main__":
    get_objects("application-sites", fields)

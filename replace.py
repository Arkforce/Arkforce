domain  = input("Enter the domail name: ")
domain_name = domain.removeprefix("www.").removesuffix(".com")

print(f"YOur domain name {domain_name}")

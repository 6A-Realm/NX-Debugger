import disnake

# Embed builder
async def build(self, ctx, title_code, error_hex, error_resp, module_name, error_module, error_desc):
    embed = disnake.Embed(
        title = f"{title_code} / {error_hex}",
        description = error_resp,
        color = disnake.Colour.random(),
    )
    embed.add_field(
        name="Module",
        value = f"{module_name} ({error_module})",
        inline = True
    )
    embed.add_field(
        name = "Description",
        value = error_desc,
        inline = True
    )

    await ctx.send(embed = embed)
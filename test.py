import imgui
imgui.ImGui.CreateContext()

#As per https://github.com/ocornut/imgui/blob/8bcac7d95caa7e3b960b7bf7c3bcda4ecfe4541f/examples/imgui_impl_glfw.cpp#L150
io = imgui.ImGui.GetIO()
io.BackendPlatformName = "imgui_impl_test" #This should be setable
print(io.BackendPlatformName)

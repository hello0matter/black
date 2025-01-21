function hook_java() {
    Java.perform(function () {
        let RandomStringUtils = Java.use("org.apache.commons.lang3.RandomStringUtils");
        let randomStr = RandomStringUtils.randomAlphabetic(10)
        randomStr = "VSmPovElWH"
        console.log("\nrandomStr --> " + randomStr)
        let e_arg = Java.use("java.lang.String").$new("pediy_imyang_").concat(randomStr)
        console.log("e_arg --> " + e_arg)
        e_arg = Java.use("java.lang.String").$new(e_arg).getBytes()
        console.log("e_arg_bytes --> " + e_arg)
        let MainObj = null
        Java.choose("com.kanxue.ollvm5.MainActivity", {
            onMatch(instance) {
                MainObj = instance
            }, onComplete() {

            }
        })
        let e_ret = MainObj.e(e_arg)
        console.log("func e_ret --> " + e_ret)
        let ByteString = Java.use("okio.ByteString")
        let hex_txt = ByteString.of(e_ret).hex()
        console.log("hex_txt --> " + hex_txt)
    })
}
setImmediate(hook_java)

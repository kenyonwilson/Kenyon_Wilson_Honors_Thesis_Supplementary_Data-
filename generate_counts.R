data <- data.frame(read.table("nonsyn.tab",header=F,sep="|"))
data2 <- matrix(0,dim(data)[1],dim(data)[2])

for(i in 1:dim(data)[2]){
        a <- table(data[,i])
        if(a[1] <= a[2]){data2[which(data[,i] == names(a)[1]),i] <- 1}
        else {data2[which(data[,i] == names(a)[2]),i] <- 1}
}


write.table(t(data2),file="total_nonSyn.tab",sep=" ",row.names=FALSE,col.names=FALSE,append=TRUE,quote=FALSE)



data <- data.frame(read.table("syn.tab",header=F,sep="|"))
data2 <- matrix(0,dim(data)[1],dim(data)[2])

for(i in 1:dim(data)[2]){
        a <- table(data[,i])
        if(a[1] <= a[2]){data2[which(data[,i] == names(a)[1]),i] <- 1}
        else {data2[which(data[,i] == names(a)[2]),i] <- 1}
}

write.table(t(data2),file="total_Syn.tab",sep=" ",row.names=FALSE,col.names=FALSE,append=TRUE,quote=FALSE)
~                                                                                                         
~                        
